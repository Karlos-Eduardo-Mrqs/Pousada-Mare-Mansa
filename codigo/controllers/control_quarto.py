from models.quarto import Quarto, QuartoDAO
import sqlite3

class QuartoController:
    def __init__(self, db_path="pousada.db"):
        self.conn = sqlite3.connect(db_path)
        self.quarto_dao = QuartoDAO(self.conn)
        self.quarto_dao.criar_tabela()

    def adicionar_quarto(self, numero_quarto, disponibilidade, capacidade, tipo):
        quarto = Quarto(numero_quarto, disponibilidade, capacidade, tipo)
        self.quarto_dao.inserir(quarto)

    def listar_quartos(self):
        return self.quarto_dao.buscar_todos()

    def atualizar_quarto(self, quarto: Quarto):
        self.quarto_dao.atualizar(quarto)

    def remover_quarto(self, numero_quarto):
        self.quarto_dao.deletar(numero_quarto)

    def fechar_conexao(self):
        self.conn.close()