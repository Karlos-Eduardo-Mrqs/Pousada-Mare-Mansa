import tkinter as tk
from tkinter import messagebox

# Importa as funções/modulares de interface
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

        # Banco de dados e controladores
        try:
            self.banco = Banco()
            self.banco.conectar()
            self.banco.criar_tabelas()

            self.agendamento_controller = self.banco.control_agendamento
            self.cliente_controller = self.banco.control_cliente
            self.quarto_controller = self.banco.control_quarto

            # Tela inicial só é aberta se não houver erro
            self.abrir_tela_login()

        except Exception as e:
            import traceback
            traceback.print_exc()
            messagebox.showerror("Erro crítico", f"Erro ao iniciar o banco de dados:\n{e}")
            self.root.destroy()

    def limpar_tela(self):
        if not self.root.winfo_exists():
            return
        for widget in self.root.winfo_children():
            widget.destroy()

    # Chamadas de telas
    def abrir_tela_login(self):
        self.limpar_tela()
        TelaLogin(self.root, self)

    def abrir_tela_menu(self):
        self.limpar_tela()
        TelaMenu(self.root, self)

    def abrir_agendamentos(self):
        self.limpar_tela()
        TelaAgendamento(self.root, self)

    def abrir_logs(self):
        self.limpar_tela()
        TelaLogs(self)

    def voltar_menu(self):
        self.root.after(100, self.abrir_tela_menu)

    def sair(self):
        self.banco.desconectar()
        self.root.destroy()

# Executa o app
if __name__ == "__main__":
    root = tk.Tk()
    app = TelasPousada(root)
    root.mainloop()
