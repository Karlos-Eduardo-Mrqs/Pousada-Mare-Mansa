import sqlite3

class Control_Quarto:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def criar_tabela(self):
        """Cria a tabela quartos no banco (se não existir)"""
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS quartos (
                numero_quarto INTEGER PRIMARY KEY,
                disponivel INTEGER NOT NULL DEFAULT 1,
                capacidade INTEGER NOT NULL,
                tipo_id INTEGER,
                FOREIGN KEY(tipo_id) REFERENCES tipos(id)
            )
        """)
        self.conn.commit()

    def adicionar_quarto(self, numero_quarto: int, disponivel: bool, capacidade: int, tipo_id: int):
        """Adiciona um novo quarto"""
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO quartos (numero_quarto, disponivel, capacidade, tipo_id) VALUES (?, ?, ?, ?)",
            (numero_quarto, int(disponivel), capacidade, tipo_id)
        )
        self.conn.commit()

    def remover_quarto(self, numero_quarto: int):
        """Remove um quarto pelo número"""
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM quartos WHERE numero_quarto = ?", (numero_quarto,))
        self.conn.commit()

    def listar_quartos(self):
        """Lista todos os quartos cadastrados"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM quartos")
        rows = cursor.fetchall()
        return [
            {
                "numero_quarto": row[0],
                "disponivel": bool(row[1]),
                "capacidade": row[2],
                "tipo_id": row[3]
            } for row in rows
        ]

    def atualizar_status_quarto(self, disponivel: bool, numero_quarto: int):
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE quartos SET disponivel = ? WHERE numero_quarto = ?",
            (int(disponivel), numero_quarto)
        )
        self.conn.commit()