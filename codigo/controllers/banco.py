import os
import sqlite3

from models.cliente import ClienteDAO
from models.quarto import QuartoDAO
from models.agendamento import AgendamentoDAO
from models.usuario import UsuarioDAO
from models.tipo import TipoDAO

from controllers.control_agendamento import AgendamentoController
from controllers.control_cliente import ClienteController
from controllers.control_quarto import QuartoController

class Banco:
    def __init__(self, nome_banco='pousada.db'):
        self.conn = None
        self.nome_banco = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", nome_banco)

        # Inicializa os atributos dos controllers como None
        self.control_agendamento = None
        self.control_cliente = None
        self.control_quarto = None

    def conectar(self):
        try:
            self.conn = sqlite3.connect(self.nome_banco)
            print("✅ Conexão estabelecida com sucesso.")

            # Instancia os controllers com a conexão
            self.control_agendamento = AgendamentoController()
            self.control_cliente = ClienteController()
            self.control_quarto = QuartoController()

            return self.conn
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
            UsuarioDAO(self.conn).criar_tabela()
            TipoDAO(self.conn).criar_tabela()
            QuartoDAO(self.conn).criar_tabela()
            ClienteDAO(self.conn).criar_tabela()
            AgendamentoDAO(self.conn).criar_tabela()
        else:
            print("⚠️ Conexão não estabelecida. Não é possível criar tabelas.")
