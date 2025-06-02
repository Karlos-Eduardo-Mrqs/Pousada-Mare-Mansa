from dataclasses import dataclass

@dataclass
class Cliente:
    cpf: str
    nome: str
    email: str

class ClienteDAO:
    def __init__(self, conn):
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

    def inserir(self, cliente: Cliente):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO Cliente (cpf, nome, email) VALUES (?, ?, ?);",
            (cliente.cpf, cliente.nome, cliente.email)
        )
        self.conn.commit()

    def atualizar(self, cliente: Cliente):
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE Cliente SET nome = ?, email = ? WHERE cpf = ?;",
            (cliente.nome, cliente.email, cliente.cpf)
        )
        self.conn.commit()

    def deletar(self, cpf: str):
        cursor = self.conn.cursor()
        cursor.execute(
            "DELETE FROM Cliente WHERE cpf = ?;",
            (cpf,)
        )
        self.conn.commit()

    def listar(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT cpf, nome, email FROM Cliente;")
        rows = cursor.fetchall()
        return [Cliente(*row) for row in rows]

    def buscar_por_cpf(self, cpf: str):
        cursor = self.conn.cursor()
        cursor.execute("SELECT cpf, nome, email FROM Cliente WHERE cpf = ?;", (cpf,))
        row = cursor.fetchone()
        return Cliente(*row) if row else None