from dataclasses import dataclass
import sqlite3

@dataclass
class Control_Cliente:
    conn: sqlite3.Connection

    def criar_tabela(self):
        cursor = self.conn.cursor()
        cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS Cliente (
                cpf TEXT PRIMARY KEY,
                nome TEXT,
                email TEXT
            );
        """
        )
        self.conn.commit()
        print("Tabela Cliente criada com sucesso.")