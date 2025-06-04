from datetime import date
from typing import List, Dict

class Control_Agendamento:
    def __init__(self, conn):
        self.conn = conn

    def criar_tabela(self) -> None:
        """Cria a tabela agendamentos no banco (se não existir)"""
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS agendamentos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data_entrada TEXT NOT NULL,
                data_saida TEXT NOT NULL,
                cpf TEXT,
                quarto_id INTEGER,
                FOREIGN KEY(cpf) REFERENCES clientes(cpf),
                FOREIGN KEY(quarto_id) REFERENCES quartos(numero_quarto)
            )
        """)
        self.conn.commit()

    def adicionar_agendamento(self, data_entrada: date, data_saida: date, cpf: str, numero_quarto: int) -> int:
        """Adiciona um novo agendamento e retorna o id criado"""
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO agendamentos (data_entrada, data_saida, cpf, quarto_id) VALUES (?, ?, ?, ?)",
            (data_entrada, data_saida, cpf, numero_quarto)
        )
        self.conn.commit()
        return cursor.lastrowid

    def remover_agendamento(self, agendamento_id: int) -> None:
        """Remove um agendamento pelo ID"""
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM agendamentos WHERE id = ?", (agendamento_id,))
        self.conn.commit()

    def listar_agendamentos(self) -> List[Dict]:
        """Retorna uma lista de agendamentos com dados completos"""
        cursor = self.conn.cursor()
        query = '''
            SELECT ag.id, cl.nome, ag.data_entrada, ag.data_saida, cl.cpf, cl.email, ag.numero_quarto
            FROM agendamentos ag JOIN clientes cl ON ag.cliente_cpf = cl.cpf
        '''

        cursor.execute(query)
        rows = cursor.fetchall()

        agendamentos = []
        for row in rows:
            agendamentos.append({
                'id': row[0],
                'nome': row[1],
                'email': row[2],
                'data_entrada': row[3],
                'data_saida': row[4],
                'cpf': row[5],
                'quarto': row[6],
                'tipo': row[7],
                'preco': float(row[8]),
            })
        return agendamentos

    def carregar_dados(self) -> List[Dict]:
        """Carrega dados formatados para a interface"""
        agendamentos = self.listar_agendamentos()
        dados_formatados = []
        for ag in agendamentos:
            dados_formatados.append({
                "id": ag["id"],
                "nome": ag["nome"],
                "data": f"{ag['data_entrada']} a {ag['data_saida']}",
                "quarto": ag["quarto"]
            })
        return dados_formatados

    def atualizar_agendamento(self, id_agendamento: int, data_entrada: date, data_saida: date, cpf: str, numero_quarto: int) -> None:
        """Atualiza os dados do agendamento pelo ID"""
        cursor = self.conn.cursor()
        cursor.execute("""
            UPDATE agendamentos
            SET data_entrada = ?, data_saida = ?, cpf = ?, quarto_id = ?
            WHERE id = ?
        """, (data_entrada, data_saida, cpf, numero_quarto, id_agendamento))
        self.conn.commit()