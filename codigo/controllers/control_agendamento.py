import sqlite3
from datetime import date

class Control_Agendamento:
    def __init__(self, conn: sqlite3.Connection):
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
        return cursor.lastrowid  # Retorna o ID do agendamento criado

    def remover_agendamento(self, agendamento_id: int):
        """Remove um agendamento pelo ID"""
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM agendamentos WHERE id = ?", (agendamento_id,))
        self.conn.commit()

    def listar_agendamentos(self):
        """Lista todos os agendamentos cadastrados"""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT id, data_entrada, data_saida, cpf, numero FROM agendamentos
        """)
        rows = cursor.fetchall()
        return [
            {
                "id": row[0],
                "data_entrada": row[1],
                "data_saida": row[2],
                "cpf": row[3],
                "numero_quarto": row[4]
            } for row in rows
        ]
