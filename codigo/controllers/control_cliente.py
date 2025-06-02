from models.cliente import Cliente, ClienteDAO
import sqlite3

class ClienteController:
    def __init__(self, db_path="pousada.db"):
        self.conn = sqlite3.connect(db_path)
        self.cliente_dao = ClienteDAO(self.conn)
        self.cliente_dao.criar_tabela()

    def adicionar_cliente(self, cpf, nome, email):
        cliente = Cliente(cpf, nome, email)
        self.cliente_dao.inserir(cliente)

    def atualizar_cliente(self, cpf, nome, email):
        cliente = Cliente(cpf, nome, email)
        self.cliente_dao.atualizar(cliente)

    def remover_cliente(self, cpf):
        self.cliente_dao.deletar(cpf)

    def buscar_cliente_por_cpf(self, cpf):
        return self.cliente_dao.buscar_por_cpf(cpf)

    def listar_clientes(self):
        return self.cliente_dao.listar()

    def fechar_conexao(self):
        self.conn.close()