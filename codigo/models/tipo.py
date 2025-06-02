from dataclasses import dataclass

@dataclass
class Tipo:
    id: int
    nome: str
    preco: float

class TipoDAO:
    def __init__(self, conn):
        self.conn = conn

    def criar_tabela(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Tipo (
                id INTEGER PRIMARY KEY,
                nome TEXT NOT NULL,
                preco REAL NOT NULL
            );
        """)
        self.conn.commit()

    def inserir(self, tipo: Tipo):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO Tipo (id, nome, preco) VALUES (?, ?, ?);
        """, (tipo.id, tipo.nome, tipo.preco))
        self.conn.commit()

    def buscar_todos(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, nome, preco FROM Tipo;")
        return [Tipo(*linha) for linha in cursor.fetchall()]

    def atualizar(self, tipo: Tipo):
        cursor = self.conn.cursor()
        cursor.execute("""
            UPDATE Tipo SET nome = ?, preco = ? WHERE id = ?;
        """, (tipo.nome, tipo.preco, tipo.id))
        self.conn.commit()

    def deletar(self, id: int):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM Tipo WHERE id = ?;", (id,))
        self.conn.commit()