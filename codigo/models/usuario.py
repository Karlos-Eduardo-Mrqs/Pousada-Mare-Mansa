from dataclasses import dataclass

@dataclass
class Usuario:
    id: int
    nome: str
    email: str
    senha: str

class UsuarioDAO:
    def __init__(self, conn):
        self.conn = conn

    def criar_tabela(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Usuario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                senha TEXT NOT NULL
            );
        """)
        self.conn.commit()

    def adicionar_usuario(self, usuario: Usuario):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO Usuario (nome, email, senha) VALUES (?, ?, ?);",
            (usuario.nome, usuario.email, usuario.senha)
        )
        self.conn.commit()  

    def remover_usuario(self, id: int):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM Usuario WHERE id = ?;", (id,))
        self.conn.commit()

    def autenticar(self, nome: str, senha: str):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT id, nome, email, senha FROM Usuario WHERE nome = ? AND senha = ?;",
            (nome, senha)
        )
        row = cursor.fetchone()
        return Usuario(*row) if row else None

    def listar_usuarios(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, nome, email, senha FROM Usuario")
        rows = cursor.fetchall()
        return [Usuario(*row) for row in rows]