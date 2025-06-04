import os
import sqlite3

from .control_tipo import Control_Tipo
from .control_quarto import Control_Quarto
from .control_cliente import Control_Cliente
from .control_agendamento import Control_Agendamento
from .control_usuario import Control_Usuario

class Banco:
    def __init__(self, nome_banco='pousada.db'):
        self.conn = None
        self.nome_banco = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", nome_banco)

    def conectar(self):
        try:
            self.conn = sqlite3.connect(self.nome_banco)
            print("✅ Conexão estabelecida com sucesso.")
        except sqlite3.Error as erro:
            print(f"❌ Erro ao conectar ao banco: {erro}")
            raise

    def desconectar(self):
        if self.conn:
            self.conn.close()
            self.conn = None
            print("🔌 Conexão encerrada.")

    def criar_tabelas(self):
        if self.conn:
            self.control_usuario = Control_Usuario(self.conn)
            self.control_usuario.criar_tabela()

            self.control_tipo = Control_Tipo(self.conn)
            self.control_tipo.criar_tabela()

            self.control_quarto = Control_Quarto(self.conn)
            self.control_quarto.criar_tabela()

            self.control_cliente = Control_Cliente(self.conn)
            self.control_cliente.criar_tabela()

            self.control_agendamento = Control_Agendamento(self.conn)
            self.control_agendamento.criar_tabela()

            if not self.control_tipo.listar_tipos():
                print("Inserindo tipos de quartos iniciais...")
                self.control_tipo.adicionar_tipo(1, "Quarto Solteiro", 100.00)
                self.control_tipo.adicionar_tipo(2, "Quarto Casal", 150.00)
                self.control_tipo.adicionar_tipo(3, "Suíte", 250.00)
                self.control_tipo.adicionar_tipo(4, "Suíte Luxo", 400.00)
                self.control_tipo.adicionar_tipo(5, "Apartamento Familiar", 350.00)

            if not self.control_quarto.listar_quartos():
                self.control_quarto.adicionar_quarto(101, True, 2, 1)
                self.control_quarto.adicionar_quarto(102, True, 2, 1)
                self.control_quarto.adicionar_quarto(201, True, 4, 2)
                self.control_quarto.adicionar_quarto(202, True, 4, 2)
                self.control_quarto.adicionar_quarto(301, True, 6, 3)
                self.control_quarto.adicionar_quarto(302, True, 6, 3)
                print("Dados iniciais de quartos inseridos.")
        else:
            print("⚠️ Conexão não estabelecida.")
