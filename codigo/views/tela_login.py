import tkinter as tk
from tela_logs import TelaLogs

class TelaLogin:
    def __init__(self, app):
        self.app = app
        self.app.limpar_tela()
        self.app.root.title("Login - Pousada Maré Mansa")

        self.frame = tk.Frame(self.app.root)
        self.frame.pack(pady=20)
        # registrar_log(nome_usuario, "Realizou login no sistema")

        tk.Label(self.frame, text="Tela de Login", font=("Arial", 16, "bold")).pack(pady=10)
        tk.Button(self.frame, text="Voltar", command=self.app.abrir_tela_gerenciamento).pack(pady=5)
