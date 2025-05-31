import tkinter as tk

class TelaMenu:
    def __init__(self, app):
        self.app = app
        self.app.limpar_tela()
        self.app.root.title("Pousada Maré Mansa - Menu Principal")

        self.frame = tk.Frame(self.app.root)
        self.frame.pack(pady=20)

        tk.Label(self.frame, text="Sistema de Gestão da Pousada Maré Mansa", font=("Arial", 14, "bold")).pack(pady=10)

        botoes = [
            ("Gerenciar Agendamentos", self.app.abrir_agendamentos),
            #("Gerenciar Quartos", self.app.abrir_quartos),
            ("Sair", self.app.sair)
        ]

        for texto, comando in botoes:
            tk.Button(self.frame, text=texto, width=30, command=comando).pack(pady=5)