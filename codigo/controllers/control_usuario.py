from models.usuario import Usuario, UsuarioDAO
from controllers.banco import Banco

class ControlUsuario:
    def __init__(self):
        self.banco = Banco()
        self.banco.conectar()
        self.usuario_dao = UsuarioDAO(self.banco.conn)
        self.usuario_dao.criar_tabela()

    def criar_usuario(self, nome: str, email: str, senha: str):
        # Aqui você poderia adicionar validações (exemplo: email válido, senha forte)
        novo_usuario = Usuario(id=0, nome=nome, email=email, senha=senha)
        self.usuario_dao.adicionar_usuario(novo_usuario)

    def remover_usuario(self, id: int):
        self.usuario_dao.remover_usuario(id)

    def autenticar_usuario(self, nome: str, senha: str):
        return self.usuario_dao.autenticar(nome, senha)

    def listar_usuarios(self):
        return self.usuario_dao.listar_usuarios()

    def fechar_conexao(self):
        self.banco.desconectar()