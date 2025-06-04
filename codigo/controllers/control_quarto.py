import sqlite3

class Control_Quarto:
    def __init__(self, conn):
        self.conn = conn

    def criar_tabela(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS quartos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tipo TEXT NOT NULL,
                preco REAL NOT NULL,
                status INTEGER NOT NULL
            )
        ''')
        self.conn.commit()

    def adicionar_quarto(self, numero_quarto: int, disponivel: bool, capacidade: int, tipo_id: int):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO quartos (numero_quarto, disponibilidade, capacidade, tipo_id) VALUES (?, ?, ?, ?)",
            (numero_quarto, int(disponivel), capacidade, tipo_id)
        )
        self.conn.commit()

    def remover_quarto(self, numero_quarto: int):
        """Remove um quarto pelo número"""
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM quartos WHERE numero_quarto = ?", (numero_quarto,))
        self.conn.commit()

    def listar_quartos(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT numero_quarto, disponibilidade, capacidade, tipo_id FROM quartos")
        resultado = cursor.fetchall()
        return [{"numero": row[0], "disponibilidade": row[1], "capacidade": row[2], "tipo_id": row[3]} for row in resultado]

    def atualizar_status_quarto(self, disponivel: bool, numero_quarto: int):
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE quartos SET disponibilidade = ? WHERE numero_quarto = ?",
            (int(disponivel), numero_quarto)
        )
        self.conn.commit()