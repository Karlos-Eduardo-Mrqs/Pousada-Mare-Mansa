from dataclasses import dataclass
from models.agendamento import Agendamento
import sqlite3

@dataclass
class Control_Agendamento:
    conn: sqlite3.Connection
    def __init__(self, ger_agendamento , control_cliente , control_quarto ):
        self.__ger_agendamento = ger_agendamento
        self.__control_cliente = control_cliente
        self.__control_quarto = control_quarto

    def criar_tabela(self):
        cursor = self.conn.cursor()
        cursor.execute(
        """ 
            CREATE TABLE IF NOT EXISTS Agendamento (
                id INTEGER PRIMARY KEY,
                data_entrada TEXT,         -- formato DD-MM-YYYY
                data_saida TEXT,           -- formato DD-MM-YYYY
                cpf TEXT,
                numero TEXT,
                FOREIGN KEY(cpf) REFERENCES Cliente(cpf),
                FOREIGN KEY(numero) REFERENCES Quarto(numero)
            );
        """
        )    
        self.conn.commit()
        print("Tabela Agendamento criada com sucesso.")

        def criar_agendamento(self, data_entrada:str, data_saida:str, cpf:str, numero_quarto:int):
            cliente = self.__control_cliente.buscar_cliente_por_cpf(cpf)
            if not cliente:
                raise Exception("Cliente não encontrado.")

            quarto = self.__control_quarto.buscar_quarto_por_numero(numero_quarto)
            if not quarto:
                raise Exception("Quarto não encontrado.")

            novo_agendamento = Agendamento(
                id=None,  # O ID será gerado pelo banco
                data_entrada=data_entrada,
                data_saida=data_saida,
                cliente=cliente,
                quarto=quarto
            )

            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO Agendamento (data_entrada, data_saida, cpf, numero) VALUES (?, ?, ?, ?)",
                (data_entrada.strftime('%d/%m/%Y'), data_saida.strftime('%d/%m/%Y'), cpf, numero_quarto)
            )
            self.conn.commit()

            novo_agendamento.id = cursor.lastrowid  # Define o ID do novo agendamento
            self.__ger_agendamento.adicionar_agendamento(novo_agendamento)
            return novo_agendamento

    def excluir_agendamento(self, cpf, numero_quarto):
        cliente = self.__control_cliente.buscar_cliente_por_cpf(cpf)
        if not cliente:
            raise Exception("Cliente não encontrado.")

        numero_quarto = int(numero_quarto)
        agendamentos = self.__ger_agendamento.get_agendamentos()

        for agendamento in agendamentos:
            if agendamento.cliente.cpf == cpf and agendamento.quarto.numero_quarto == numero_quarto:
                self.__ger_agendamento.remover_agendamento(agendamento)
                return

        raise Exception("Agendamento não encontrado.")

    def listar_agendamentos(self):
        return self.__ger_agendamento.get_agendamentos()