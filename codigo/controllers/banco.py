import os
import sqlite3
from .control_tipo import Control_Tipo
from .control_agendamento import Control_Agendamento
from .control_quarto import Control_Quarto
from .control_cliente import Control_Cliente

class Banco: 
    def __init__(self, nome_banco='pousada.db'):
        self.conn = None
        self.nome_banco = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', nome_banco)

    def conectar(self):
        try:
            self.conn = sqlite3.connect(self.nome_banco)
            print("Conexão estabelecida com sucesso.")
        except sqlite3.Error as erro:
            print(f"Ocorreu um erro na conexão: {erro}")
            raise
    
    def desconectar(self):
        if self.conn:
            self.conn.close()
            self.conn = None
            print("Conexão encerrada.")
    
    def criar_tabelas(self):
        if self.conn:
            controle_tipo = Control_Tipo(self.conn)
            controle_tipo.criar_tabela()

            controle_quarto = Control_Quarto(self.conn)
            controle_quarto.criar_tabela()

            controle_cliente = Control_Cliente(self.conn)
            controle_cliente.criar_tabela()

            controle_agendamento = Control_Agendamento(self.conn)
            controle_agendamento.criar_tabela()
        else:
            print("Conexão não estabelecida. Não é possível criar tabelas.")