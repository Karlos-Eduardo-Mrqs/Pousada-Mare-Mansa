import sqlite3 

try:
    print("Iniciando...")

    conn = sqlite3.connect('pousada.db')
    cursor = conn.cursor()

    sql_script = '''
    CREATE TABLE IF NOT EXISTS Cliente (
        cpf TEXT PRIMARY KEY,
        nome TEXT,
        email TEXT
    );

    CREATE TABLE IF NOT EXISTS Tipo (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        preco REAL
    );

    CREATE TABLE IF NOT EXISTS Quarto (
        numero TEXT PRIMARY KEY,
        disponibilidade TEXT,
        capacidade INTEGER,
        id INTEGER,
        FOREIGN KEY(id) REFERENCES Tipo(id)
    );

    CREATE TABLE IF NOT EXISTS Agendamento (
        id INTEGER PRIMARY KEY,
        data_entrada TEXT,
        data_saida TEXT,
        cpf TEXT,
        numero INTEGER,
        FOREIGN KEY(cpf) REFERENCES Cliente(cpf),
        FOREIGN KEY(numero) REFERENCES Quarto(numero)
    );
    '''

    cursor.executescript(sql_script)
    conn.commit()
    conn.close()

    print("Banco de dados criado com sucesso!")

except Exception as e:
    print("Ocorreu um erro:", e)