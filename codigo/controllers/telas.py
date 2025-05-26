import tkinter as tk
from tkinter import ttk
from controllers.banco import Banco

class TelasPython:
    def __init__(self, root):
        self.root = root
        self.abrir_tela_gerenciamento()
        # self.abrir_tela_login()

    def limpar_tela(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def abrir_tela_login(self):
        # Aqui será realizada a tela de login pelo programador Gabriel Morais 
        self.limpar_tela()
        self.root.title("Pousada Maré Mansa - Login")
        self.root.geometry("500x400")

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        tk.Label(self.frame, text="Login", font=("Arial", 14, "bold")).pack(pady=10)
        tk.Button(self.frame, text="Sair", command=self.root.destroy).pack(pady=10)

    def abrir_tela_gerenciamento(self):
        self.limpar_tela()
        self.root.title("Pousada Maré Mansa")
        self.root.geometry("500x400")

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        tk.Label(self.frame, text="Sistema de Gestão - Pousada Maré Mansa", font=("Arial", 14, "bold")).pack(pady=10)

        tk.Button(self.frame, text="Gerenciar Agendamentos", width=25, command=self.abrir_agendamentos).pack(pady=10)
        tk.Button(self.frame, text="Relatórios", width=25, command=self.abrir_relatorios).pack(pady=10)
        tk.Button(self.frame, text="Sair", width=25, command=self.sair).pack(pady=20)

    def abrir_clientes(self):
        self.limpar_tela()
        self.root.title("Pousada Maré Mansa - Clientes")
        self.root.geometry("500x400")

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        tk.Label(self.frame, text="Clientes", font=("Arial", 14, "bold")).pack(pady=10)
        tk.Button(self.frame, text="Voltar", command=self.abrir_tela_gerenciamento).pack(pady=10)

    def abrir_quartos(self):
        self.limpar_tela()
        self.root.title("Pousada Maré Mansa - Quartos")
        self.root.geometry("500x400")

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        tk.Label(self.frame, text="Quartos", font=("Arial", 14, "bold")).pack(pady=10)
        tk.Button(self.frame, text="Voltar", command=self.abrir_tela_gerenciamento).pack(pady=10)

    def abrir_tipos(self):
        self.limpar_tela()
        self.root.title("Pousada Maré Mansa - Tipos de Quarto")
        self.root.geometry("500x400")

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        tk.Label(self.frame, text="Tipos de Quarto", font=("Arial", 14, "bold")).pack(pady=10)
        tk.Button(self.frame, text="Voltar", command=self.abrir_tela_gerenciamento).pack(pady=10)

    def abrir_agendamentos(self):
        self.limpar_tela()
        self.root.title("Pousada Maré Mansa - Agendamentos")
        self.root.geometry("500x400")

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        tk.Label(self.frame, text="Agendamentos", font=("Arial", 14, "bold")).pack(pady=10)
        tk.Button(self.frame, text="Voltar", command=self.abrir_tela_gerenciamento).pack(pady=10)

    def sair(self):
        self.root.destroy()

# Execução da aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = TelasPython(root)
    root.mainloop()
