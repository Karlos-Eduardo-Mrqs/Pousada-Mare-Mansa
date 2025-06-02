from models.cliente import Cliente

class Control_Cliente:
    def __init__(self, conn):
        self.conn = conn

    def criar_tabela(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Cliente (
                cpf TEXT PRIMARY KEY,
                nome TEXT NOT NULL,
                email TEXT
            )
        """)
        self.conn.commit()

    def adicionar_cliente(self, cpf: str, nome: str, email: str):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO Cliente (cpf, nome, email) VALUES (?, ?, ?)",
            (cpf, nome, email)
        )
        self.conn.commit()

    def remover_cliente(self, cpf: str):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM Cliente WHERE cpf = ?", (cpf,))
        self.conn.commit()

    def listar_clientes(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Cliente")
        rows = cursor.fetchall()
        return [Cliente(cpf=row[0], nome=row[1], email=row[2]) for row in rows]

    def buscar_cliente_por_cpf(self, cpf: str):
        """Retorna o cliente do CPF informado"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Cliente WHERE cpf = ?", (cpf,))
        resultado = cursor.fetchone()
        if resultado:
            return {"cpf": resultado[0], "nome": resultado[1], "email": resultado[2]}
        return None