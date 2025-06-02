import sqlite3
from dataclasses import dataclass

@dataclass
class Quarto:
    numero_quarto: int
    disponibilidade: bool
    capacidade: int
    tipo: int  # assumo que tipo é um FK para Tipo(id)

class QuartoDAO:
    def __init__(self, conn):
        self.conn = conn

    def criar_tabela(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Quarto (
                numero_quarto INTEGER PRIMARY KEY,
                disponibilidade INTEGER NOT NULL DEFAULT 1,
                capacidade INTEGER NOT NULL,
                tipo INTEGER,
                FOREIGN KEY(tipo) REFERENCES Tipo(id)
            );
        """)
        self.conn.commit()

    def inserir(self, quarto: Quarto):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO Quarto (numero_quarto, disponibilidade, capacidade, tipo)
            VALUES (?, ?, ?, ?);
        """, (quarto.numero_quarto, int(quarto.disponibilidade), quarto.capacidade, quarto.tipo))
        self.conn.commit()

    def buscar_todos(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT numero_quarto, disponibilidade, capacidade, tipo FROM Quarto;")
        rows = cursor.fetchall()
        return [Quarto(row[0], bool(row[1]), row[2], row[3]) for row in rows]

    def atualizar(self, quarto: Quarto):
        cursor = self.conn.cursor()
        cursor.execute("""UPDATE Quarto SET disponibilidade = ?, capacidade = ?, tipo = ? WHERE numero_quarto = ?;
        """, (int(quarto.disponibilidade), quarto.capacidade, quarto.tipo, quarto.numero_quarto))
        self.conn.commit()

    def deletar(self, numero_quarto: int):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM Quarto WHERE numero_quarto = ?;", (numero_quarto,))
        self.conn.commit()