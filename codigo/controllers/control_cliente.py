class Control_Cliente:
    def __init__(self, conn):
        self.conn = conn
    
    def criar_tabela(self):
        """Cria a tabela clientes no banco (se não existir)"""
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                cpf TEXT PRIMARY KEY,
                nome TEXT NOT NULL,
                email TEXT
            )
        """)
        self.conn.commit()

    def adicionar_cliente(self, cpf: str, nome: str, email: str):
        """Adiciona um novo cliente ao banco"""
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO clientes (cpf, nome, email) VALUES (?, ?, ?)",
            (cpf, nome, email)
        )
        self.conn.commit()

    def remover_cliente(self, cpf: str):
        """Remove um cliente pelo CPF"""
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM clientes WHERE cpf = ?", (cpf,))
        self.conn.commit()

    def listar_clientes(self):
        """Lista todos os clientes cadastrados"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM clientes")
        rows = cursor.fetchall()
        return [{"cpf": row[0], "nome": row[1], "email": row[2]} for row in rows]
