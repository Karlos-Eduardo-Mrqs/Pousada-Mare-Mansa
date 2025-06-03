import tkinter as tk
from controllers.banco import Banco

from views.tela_login import TelaLogin
from views.tela_menu import TelaMenu
from views.tela_agendamento import TelaAgendamento
from views.tela_logs import TelaLogs

class TelasPousada:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x400")
        self.root.title("Pousada Maré Mansa")

        # Instancia Banco e conecta
        self.banco = Banco()
        self.banco.conectar()         # conecta e inicializa controladores
        self.banco.inserir_dados_iniciais    # cria tabelas usando controladores

        # Pega controladores prontos para uso
        self.agendamento_controller = self.banco.control_agendamento
        self.cliente_controller = self.banco.control_cliente
        self.quarto_controller = self.banco.control_quarto

        # Tela inicial
        self.abrir_tela_login()

    def limpar_tela(self):
        if not self.root.winfo_exists():
            return
        for widget in self.root.winfo_children():
            widget.destroy()

    def abrir_tela_login(self):
        self.limpar_tela()
        TelaLogin(self.root, self, self.banco.conn)

    def abrir_tela_menu(self):
        self.limpar_tela()
        TelaMenu(self.root, self)

    def abrir_agendamentos(self):
        self.limpar_tela()
        TelaAgendamento(self.root, self, self.banco.conn)

    def abrir_logs(self):
        self.limpar_tela()
        TelaLogs(self)

    def voltar_menu(self):
        self.root.after(100, self.abrir_tela_menu)

    def sair(self):
        self.banco.desconectar()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TelasPousada(root)
    root.mainloop()