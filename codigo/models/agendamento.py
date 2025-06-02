from dataclasses import dataclass
import sqlite3
from datetime import date

@dataclass
class Agendamento:
    id: int
    data_entrada: date
    data_saida: date
    cliente_cpf: str
    numero_quarto: int

class AgendamentoDAO:
    def __init__(self, conn):
        self.conn = conn

    def criar_tabela(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Agendamento (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data_entrada DATE NOT NULL,
                data_saida DATE NOT NULL,
                cliente_cpf TEXT NOT NULL,
                numero_quarto INTEGER NOT NULL,
                FOREIGN KEY(cliente_cpf) REFERENCES Cliente(cpf),
                FOREIGN KEY(numero_quarto) REFERENCES Quarto(numero)
            );
        """)
        self.conn.commit()

    def inserir(self, agendamento: Agendamento):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO Agendamento (data_entrada, data_saida, cliente_cpf, numero_quarto)
            VALUES (?, ?, ?, ?);
        """, (agendamento.data_entrada, agendamento.data_saida,
              agendamento.cliente_cpf, agendamento.numero_quarto))
        self.conn.commit()

    def buscar_todos(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, data_entrada, data_saida, cliente_cpf, numero_quarto FROM Agendamento;")
        return [Agendamento(*row) for row in cursor.fetchall()]

    def atualizar(self, agendamento: Agendamento):
        cursor = self.conn.cursor()
        cursor.execute("""
            UPDATE Agendamento SET
                data_entrada = ?, data_saida = ?, cliente_cpf = ?, numero_quarto = ?
            WHERE id = ?;
        """, (agendamento.data_entrada, agendamento.data_saida,
              agendamento.cliente_cpf, agendamento.numero_quarto, agendamento.id))
        self.conn.commit()

    def deletar(self, id: int):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM Agendamento WHERE id = ?;", (id,))
        self.conn.commit()
