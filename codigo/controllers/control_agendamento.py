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
            (data_entrada, data_saida, cpf, numero_quarto)
        )
        self.conn.commit()
        return cursor.lastrowid

    def remover_agendamento(self, agendamento_id: int):
        """Remove um agendamento pelo ID"""
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM agendamentos WHERE id = ?", (agendamento_id,))
        self.conn.commit()

    def listar_agendamentos(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT
                a.id, c.nome, c.email, c.cpf, a.data_entrada, a.data_saida,
                q.numero_quarto, q.tipo_id, q.preco
            FROM agendamentos a
            JOIN clientes c ON a.cliente_id = c.id
            JOIN quartos q ON a.quarto = q.numero_quarto
        ''')

        resultados = cursor.fetchall()
        colunas = [desc[0] for desc in cursor.description]
        return [dict(zip(colunas, linha)) for linha in resultados]

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