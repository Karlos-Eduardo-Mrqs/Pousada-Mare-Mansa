import tkinter as tk
from controllers.banco import Banco

# Importa as funções/modulares de interface
from views.tela_login import TelaLogin
from views.tela_menu import TelaMenu
from views.tela_agendamento import TelaAgendamento  # Nome genérico da função da tela CRUD

class TelasPousada:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x400")
        self.root.title("Pousada Maré Mansa")

        # Banco de dados e controladores
        self.banco = Banco()
        self.banco.conectar()
        self.banco.criar_tabelas()

        # Controladores disponíveis para as telas
        self.agendamento_controller = self.banco.control_agendamento
        self.cliente_controller = self.banco.control_cliente
        self.quarto_controller = self.banco.control_quarto

        # Tela inicial
        self.abrir_tela_login()

    def limpar_tela(self):
        """Remove todos os elementos da tela"""
        for widget in self.root.winfo_children():
            widget.destroy()

    # Chamadas de telas
    def abrir_tela_login(self):
        self.limpar_tela()
        TelaLogin(self.root, self)  # Passa self como app

    def abrir_tela_gerenciamento(self):
        self.limpar_tela()
        TelaMenu(self)

    def abrir_agendamentos(self):
        self.limpar_tela()
        TelaAgendamento(self.root)

    def abrir_logs(self):
        self.limpar_tela()
        #TelaLogs(self)

    def sair(self):
        self.banco.desconectar()
        self.root.destroy()

# Executa o app
if __name__ == "__main__":
    root = tk.Tk()
    app = TelasPousada(root)
    root.mainloop()