from datetime import date

class Control_Agendamento:
    def __init__(self, conn):
        self.conn = conn

    def criar_tabela(self):
        """Cria a tabela agendamentos no banco (se não existir)"""
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS agendamentos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data_entrada TEXT NOT NULL,
                data_saida TEXT NOT NULL,
                cpf TEXT,
                numero INTEGER,
                FOREIGN KEY(cpf) REFERENCES clientes(cpf),
                FOREIGN KEY(numero) REFERENCES quartos(numero_quarto)
            )
        """)
        self.conn.commit()

    def adicionar_agendamento(self, data_entrada: date, data_saida: date, cpf: str, numero_quarto: int):
        """Adiciona um novo agendamento"""
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO agendamentos (data_entrada, data_saida, cpf, numero) VALUES (?, ?, ?, ?)",
            (data_entrada.strftime("%d/%m/%Y"), data_saida.strftime("%d/%m/%Y"), cpf, numero_quarto)
        )
        self.conn.commit()
        return cursor.lastrowid

    def remover_agendamento(self, agendamento_id: int):
        """Remove um agendamento pelo ID"""
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM agendamentos WHERE id = ?", (agendamento_id,))
        self.conn.commit()

    def listar_agendamentos(self):
        """Lista todos os agendamentos com nome e email do cliente"""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT 
                ag.id, ag.data_entrada, ag.data_saida,
                cl.nome, cl.cpf, cl.email,
                ag.numero
            FROM agendamentos ag
            LEFT JOIN clientes cl ON ag.cpf = cl.cpf
        """)
        rows = cursor.fetchall()
        return [
            {
                "id": row[0],
                "data_entrada": row[1],
                "data_saida": row[2],
                "nome": row[3] or "Desconhecido",
                "cpf": row[4],
                "email": row[5] or "",
                "quarto": row[6]
            } for row in rows
        ]

    def carregar_dados(self):
        agendamentos = self.listar_agendamentos()
        self.dados = []
        for ag in agendamentos:
            self.dados.append({
                "id": ag["id"],
                "nome": ag["nome"],
                "data": f"{ag['data_entrada']} a {ag['data_saida']}",
                "quarto": ag["quarto"]
            })

    def atualizar_agendamento(self,id_agendamento, data_entrada, data_saida, cpf, numero_quarto):
        cursor = self.conn.cursor()
        cursor.execute("""
            UPDATE agendamentos
            SET data_entrada = ?, data_saida = ?, cpf = ?, numero = ?
            WHERE id = ?
        """, (data_entrada, data_saida, cpf, numero_quarto, id_agendamento))
        self.conn.commit()
        self.conn.desconectar()