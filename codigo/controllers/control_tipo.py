from models.tipo import Tipo, TipoDAO
from controllers.banco import Banco

class TipoController:
    def __init__(self):
        self.banco = Banco()
        self.banco.conectar()  
        self.tipo_dao = TipoDAO(self.banco.conn)
        self.tipo_dao.criar_tabela()

    def adicionar_tipo(self, id, nome, preco):
        tipo = Tipo(id, nome, preco)
        self.tipo_dao.inserir(tipo)

    def atualizar_tipo(self, id, nome, preco):
        tipo = Tipo(id, nome, preco)
        self.tipo_dao.atualizar(tipo)

    def remover_tipo(self, id):
        self.tipo_dao.deletar(id)

    def listar_tipos(self):
        return self.tipo_dao.buscar_todos()

    def fechar_conexao(self):
        self.banco.desconectar()