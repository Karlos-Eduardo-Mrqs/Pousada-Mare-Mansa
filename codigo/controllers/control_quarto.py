from dataclasses import dataclass
import sqlite3

@dataclass
class Control_Quarto:
    conn: sqlite3.Connection

    def criar_tabela(self):
        cursor = self.conn.cursor()
        cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS Quarto (
                numero TEXT PRIMARY KEY,
                disponibilidade INTEGER,
                capacidade INTEGER,
                id INTEGER,
                FOREIGN KEY(id) REFERENCES Tipo(id)
            );
        """
        )
        self.conn.commit()
        print("Tabela Quarto criada com sucesso.")