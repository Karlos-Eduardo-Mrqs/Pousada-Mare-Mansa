from dataclasses import dataclass
import sqlite3

@dataclass
class Control_Agendamento:
    conn: sqlite3.Connection

    def criar_tabela(self):
        cursor = self.conn.cursor()
        cursor.execute(
        """ 
            CREATE TABLE IF NOT EXISTS Agendamento (
                id INTEGER PRIMARY KEY,
                data_entrada TEXT,         -- formato DD-MM-YYYY
                data_saida TEXT,           -- formato DD-MM-YYYY
                cpf TEXT,
                numero TEXT,
                FOREIGN KEY(cpf) REFERENCES Cliente(cpf),
                FOREIGN KEY(numero) REFERENCES Quarto(numero)
            );
        """
        )    
        self.conn.commit()
        print("Tabela Agendamento criada com sucesso.")