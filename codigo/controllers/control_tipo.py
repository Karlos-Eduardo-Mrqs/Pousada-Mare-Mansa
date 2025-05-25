from dataclasses import dataclass
import sqlite3

@dataclass
class Control_Tipo:
    conn: sqlite3.Connection

    def criar_tabela(self):
        cursor = self.conn.cursor()
        cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS Tipo (
                id INTEGER PRIMARY KEY,
                nome TEXT,
                preco REAL
            );
        """
        )
        self.conn.commit()
        print("Tabela Tipo criada com sucesso.")
