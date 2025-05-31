import sqlite3
from models.usuario import Usuario

class Control_Usuario:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
    
    def criar_tabela(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Usuario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT,
                senha TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def adicionar_usuario(self, cpf: str, nome: str, email: str):
        """Adiciona um novo usuario ao banco"""
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO Usuario (cpf, nome, email) VALUES (?, ?, ?)",
            (cpf, nome, email)
        )
        self.conn.commit()

    def remover_usuario(self, cpf: str):
        """Remove um usuario pelo CPF"""
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM Usuario WHERE cpf = ?", (cpf,))
        self.conn.commit()

    def autenticar(self, nome:str, senha:str):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM Usuario WHERE nome = ? AND senha = ?', (nome, senha))
        row = cursor.fetchone()
        if row:
            return Usuario(*row)
        return None

    def listar_usuarios(self):
        """Lista todos os usuarios cadastrados"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Usuario")
        rows = cursor.fetchall()
        return [{"cpf": row[0], "nome": row[1], "email": row[2]} for row in rows]