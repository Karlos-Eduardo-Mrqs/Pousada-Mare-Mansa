from models.agendamento import Agendamento, AgendamentoDAO
from datetime import date

class AgendamentoController:
    def __init__(self):
        self.dao = AgendamentoDAO(self)

    def criar_tabela(self):
        self.dao.criar_tabela()

    def adicionar_agendamento(self, data_entrada: date, data_saida: date, cliente_cpf: str, numero_quarto: int):
        agendamento = Agendamento(id = -1 ,data_entrada=data_entrada, data_saida=data_saida,
                                  cliente_cpf=cliente_cpf, numero_quarto=numero_quarto)
        self.dao.inserir(agendamento)

    def listar_agendamentos(self):
        return self.dao.buscar_todos()

    def atualizar_agendamento(self, id: int, data_entrada: date, data_saida: date,
                               cliente_cpf: str, numero_quarto: int):
        agendamento = Agendamento(id=id, data_entrada=data_entrada, data_saida=data_saida,
                                  cliente_cpf=cliente_cpf, numero_quarto=numero_quarto)
        self.dao.atualizar(agendamento)

    def remover_agendamento(self, id: int):
        self.dao.deletar(id)
