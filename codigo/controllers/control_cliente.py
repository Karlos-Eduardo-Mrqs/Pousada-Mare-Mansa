import sqlite3
from models.cliente import Cliente

class Control_Cliente:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def criar_tabela(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Cliente (
                cpf TEXT PRIMARY KEY,
                nome TEXT NOT NULL,
                email TEXT
            );
        """)
        self.conn.commit()

    def adicionar_cliente(self, cliente: Cliente):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO Cliente (cpf, nome, email) VALUES (?, ?, ?)",
            (cliente.cpf, cliente.nome, cliente.email)
        )
        self.conn.commit()

    def buscar_cliente_por_cpf(self, cpf: str) -> Cliente:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Cliente WHERE cpf = ?", (cpf,))
        row = cursor.fetchone()
        if row:
            return Cliente(cpf=row[0], nome=row[1], email=row[2])
        return None

    def listar_clientes(self) -> list[Cliente]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Cliente")
        rows = cursor.fetchall()
        return [Cliente(cpf=row[0], nome=row[1], email=row[2]) for row in rows]

    def atualizar_cliente(self, cpf: str, novo_nome: str, novo_email: str):
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE Cliente SET nome = ?, email = ? WHERE cpf = ?",
            (novo_nome, novo_email, cpf)
        )
        self.conn.commit()

    def remover_cliente(self, cpf: str):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM Cliente WHERE cpf = ?", (cpf,))
        self.conn.commit()