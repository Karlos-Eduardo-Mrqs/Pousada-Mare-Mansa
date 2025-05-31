import tkinter as tk

class TelaMenu:
    def __init__(self, app):
        self.app = app
        self.app.limpar_tela()
        self.app.root.title("Pousada Maré Mansa - Menu Principal")

        self.frame = tk.Frame(self.app.root, bg="#FCEBD5")
        self.frame.pack(pady=40, padx=20, fill=tk.BOTH, expand=True)

        tk.Label(
            self.frame,
            text="Sistema de Gestão da Pousada Maré Mansa",
            font=("Arial", 16, "bold"),
            bg="#FCEBD5"
        ).pack(pady=20)

        botoes = [
            ("Gerenciar Agendamentos", self.app.abrir_agendamentos),
            # ("Gerenciar Quartos", self.app.abrir_quartos),
            ("Visualizar Relatórios (Logs)", self.app.abrir_logs),
            ("Sair", self.app.sair)
        ]

        for texto, comando in botoes:
            tk.Button(self.frame,text=texto,font=("Arial", 12),width=35,height=2,bg="#E3C9A8",command=comando).pack(pady=10)