from models.quarto import Quarto 

class Control_Quarto:
    def __init__(self, conn):
        self.conn = conn

    def criar_tabela(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Quarto (
                numero INTEGER PRIMARY KEY,
                disponibilidade INTEGER NOT NULL DEFAULT 1,
                capacidade INTEGER NOT NULL,
                tipo_id INTEGER,
                FOREIGN KEY(tipo_id) REFERENCES Tipo(id)
            )
        """)
        self.conn.commit()

    def adicionar_quarto(self, numero: int, disponibilidade: bool, capacidade: int, tipo_id: int):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO Quarto (numero, disponibilidade, capacidade, tipo_id) VALUES (?, ?, ?, ?)",
            (numero, int(disponibilidade), capacidade, tipo_id)
        )
        self.conn.commit()

    def remover_quarto(self, numero_quarto: int):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM Quarto WHERE numero = ?", (numero_quarto,))
        self.conn.commit()

    def listar_quartos(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Quarto")
        rows = cursor.fetchall()
        return [
            Quarto(numero_quarto=row[0], disponibilidade=bool(row[1]), capacidade=row[2], tipo=row[3])
            for row in rows
        ]

    def atualizar_status_quarto(self, disponibilidade:bool, numero:int):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE Quarto SET disponibilidade = ? WHERE numero = ?", (disponibilidade, numero))
        self.conn.commit()