from models.tipo import Tipo

class Control_Tipo:
    def __init__(self, conn):
        self.conn = conn

    def criar_tabela(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Tipo (
                id INTEGER PRIMARY KEY,
                nome TEXT NOT NULL,
                preco REAL NOT NULL
            )
        """)
        self.conn.commit()

    def adicionar_tipo(self, tipo_id: int, nome: str, preco: float):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO Tipo (id, nome, preco) VALUES (?, ?, ?)",
            (tipo_id, nome, preco)
        )
        self.conn.commit()

    def remover_tipo(self, tipo_id: int):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM Tipo WHERE id = ?", (tipo_id,))
        self.conn.commit()

    def listar_tipos(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Tipo")
        rows = cursor.fetchall()
        return [Tipo(id=row[0], nome=row[1], preco=row[2]) for row in rows]