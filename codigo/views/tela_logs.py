import tkinter as tk
from models.logs_json import LoggerJSON
import json

from tkinter import ttk

class TelaLogs:
    def __init__(self, app):
        self.root = app.root
        self.root.title("Relatório de Atividades")
        self.root.geometry("700x400")
        self.root.configure(bg='#FCEBD5')

        tk.Label(self.root, text="Relatório de Atividades", font=("Helvetica", 16, "bold"), bg="#FCEBD5").pack(pady=10)

        colunas = ("data", "usuario", "acao")
        self.tree = ttk.Treeview(self.root, columns=colunas, show='headings')
        for col in colunas:
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, anchor=tk.CENTER)
        self.tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.carregar_logs()

    def carregar_logs(self):
        try:
            with open("logs.json", "r", encoding="utf-8") as f:
                logs = json.load(f)
                for log in logs:
                    self.tree.insert('', tk.END, values=(log["data"], log["usuario"], log["acao"]))
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = TelaLogs(root)
    root.mainloop()