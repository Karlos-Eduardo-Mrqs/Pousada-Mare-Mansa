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

        # Inicializa controladores com None; serão setados após conexão
        self.control_usuario = Control_Usuario(self.conn)
        self.control_tipo = Control_Tipo(self.conn)
        self.control_quarto = Control_Quarto(self.conn)
        self.control_cliente = Control_Cliente(self.conn)
        self.control_agendamento = Control_Agendamento(self.conn)

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
        if not self.conn:
            print("⚠️ Conexão não estabelecida. Não é possível criar tabelas.")
            return

        self.control_cliente.criar_tabela()
        self.control_tipo.criar_tabela()
        self.control_quarto.criar_tabela()
        self.control_cliente.criar_tabela()
        self.control_agendamento.criar_tabela()
        print("Tabelas criadas com sucesso.")

    def inserir_dados_iniciais(self):
        if not self.conn:
            print("⚠️ Conexão não estabelecida. Não é possível inserir dados.")
            return

        # Inserir tipos, se não existirem
        tipos_existentes = self.control_tipo.listar_tipos()
        if not tipos_existentes:
            print("Inserindo tipos de quartos iniciais...")
            tipos = [
                (1, "Quarto Solteiro", 100.00),
                (2, "Quarto Casal", 150.00),
                (3, "Suíte", 250.00),
                (4, "Suíte Luxo", 400.00),
                (5, "Apartamento Familiar", 350.00),
            ]
            for tipo_id, nome, preco in tipos:
                self.control_tipo.adicionar_tipo(tipo_id, nome, preco)
            print("Tipos de quartos inseridos com sucesso.")
        else:
            print("Tipos de quartos já existentes no banco.")

        # Inserir quartos, se não existirem
        quartos_existentes = self.control_quarto.listar_quartos()
        if not quartos_existentes:
            print("Inserindo quartos iniciais...")
            quartos = [
                (101, True, 2, 1),
                (102, True, 2, 1),
                (201, True, 4, 2),
                (202, True, 4, 2),
                (301, True, 6, 3),
                (302, True, 6, 3),
            ]
            for numero, disponivel, capacidade, tipo_id in quartos:
                self.control_quarto.adicionar_quarto(numero, disponivel, capacidade, tipo_id)
            print("Dados iniciais de quartos inseridos.")
        else:
            print("Quartos já existentes no banco.")
    
    def inicializar_aplicacoes(self):
        # Exemplo para chamar métodos de setup ao iniciar a aplicação
        self.criar_tabelas()
        self.inserir_dados_iniciais()