import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime  # Corrigido aqui!
from models.cliente import Cliente
from models.quarto import Quarto

# Simulando a importacao do banco (remova este comentario quando Banco estiver implementado)
# from controllers.banco import Banco

class TelasPousada:
    def __init__(self, root,reservas = {}):
        self.reservas = reservas
        self.root = root
        self.root.geometry("500x400")
        self.root.title("Pousada Maré Mansa")
        self.abrir_tela_login()

    def limpar_tela(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def abrir_tela_login(self):
        self.limpar_tela()
        self.root.title("Login - Pousada Maré Mansa")

        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        tk.Label(frame, text="Tela de Login", font=("Arial", 16, "bold")).pack(pady=10)
        tk.Button(frame, text="Voltar", command=self.abrir_tela_gerenciamento).pack(pady=5)

    def abrir_tela_gerenciamento(self):
        self.limpar_tela()
        self.root.title("Pousada Maré Mansa - Menu Principal")

        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        tk.Label(frame, text="Sistema de Gestão da Pousada Maré Mansa", font=("Arial", 14, "bold")).pack(pady=10)

        botoes = [
            ("Gerenciar Agendamentos", self.abrir_agendamentos),
            ("Gerenciar Quartos", self.abrir_quartos),
            ("Fazer Agendamento", self.abrir_agendamentos),
            ("Sair", self.sair)
        ]

        for texto, comando in botoes:
            tk.Button(frame, text=texto, width=30, command=comando).pack(pady=5)

    def abrir_tela_padrao(self, titulo):
        self.limpar_tela()
        self.root.title(f"Pousada Maré Mansa - {titulo}")

        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        tk.Label(frame, text=titulo, font=("Arial", 14, "bold")).pack(pady=10)
        tk.Button(frame, text="Voltar", command=self.abrir_tela_gerenciamento).pack(pady=10)

    def abrir_agendamentos(self):
        self.limpar_tela()
        self.root.title("Pousada Maré Mansa - Cadastro de Agendamento")

        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        tk.Label(frame, text="Cadastro de Agendamento", font=("Arial", 14, "bold")).pack(pady=10)

        # Nome do cliente
        tk.Label(frame, text="Nome do Cliente:").pack()
        nome_entry = tk.Entry(frame, width=30)
        nome_entry.pack(pady=5)

        # ID do quarto
        tk.Label(frame, text="ID do Quarto:").pack()
        quarto_entry = tk.Entry(frame, width=10)
        quarto_entry.pack(pady=5)

        # Seleção de data de entrada
        tk.Label(frame, text="Data de Entrada (DD/MM/AAAA):").pack()
        data_entrada_entry = tk.Entry(frame, width=20)
        data_entrada_entry.pack(pady=5)

        # Seleção de data de saída
        tk.Label(frame, text="Data de Saída (DD/MM/AAAA):").pack()
        data_saida_entry = tk.Entry(frame, width=20)
        data_saida_entry.pack(pady=5)

        def reservar():
            nome = nome_entry.get().strip()
            id_quarto = quarto_entry.get().strip()
            entrada_str = data_entrada_entry.get().strip()
            saida_str = data_saida_entry.get().strip()

            if not nome or not id_quarto or not entrada_str or not saida_str:
                messagebox.showwarning("Campos vazios", "Preencha todos os campos.")
                return

            try:
                data_entrada = datetime.strptime(entrada_str, "%d/%m/%Y").date()
                data_saida = datetime.strptime(saida_str, "%d/%m/%Y").date()
                id_quarto = int(id_quarto)
            except ValueError:
                messagebox.showerror("Erro", "Data ou ID do quarto inválido.")
                return

            cliente = Cliente(nome=nome)  # você pode ajustar para usar um ID real
            quarto = Quarto(numero_quarto=id_quarto)  # idem

            if self.agendamento_controller.existe_agendamento_na_data(data_entrada, quarto):
                messagebox.showerror("Data Ocupada", "⚠️ Este quarto já está reservado para essa data.")
            else:
                self.agendamento_controller.criar_agendamento(data_entrada, data_saida, cliente, quarto)
                messagebox.showinfo("Reserva Confirmada", f"✅ Reserva feita para {nome} no quarto {id_quarto}")
                nome_entry.delete(0, tk.END)
                quarto_entry.delete(0, tk.END)
                data_entrada_entry.delete(0, tk.END)
                data_saida_entry.delete(0, tk.END)

        tk.Button(frame, text="Reservar", command=reservar).pack(pady=10)

        def ver_reservas():
            ags = self.agendamento_controller.listar_agendamentos()
            if not ags:
                messagebox.showinfo("Reservas", "📭 Nenhuma reserva feita.")
            else:
                texto = "Reservas:\n"
                for ag in ags:
                    texto += f"{ag.data_entrada} até {ag.data_saida} -> {ag.cliente.nome} (Quarto {ag.quarto.id})\n"
                messagebox.showinfo("Reservas", texto)

        tk.Button(frame, text="Ver Reservas", command=ver_reservas).pack(pady=5)
        tk.Button(frame, text="Voltar ao Menu", command=self.abrir_tela_gerenciamento).pack(pady=10)

    def abrir_quartos(self):
        self.abrir_tela_padrao("Quartos")

    def sair(self):
        self.root.destroy()

# Execução do programa
if __name__ == "__main__":
    root = tk.Tk()
    app = TelasPousada(root)
    root.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime  # Corrigido aqui!
from models.cliente import Cliente
from models.quarto import Quarto

# Simulando a importacao do banco (remova este comentario quando Banco estiver implementado)
# from controllers.banco import Banco

class TelasPousada:
    def __init__(self, root,reservas = {}):
        self.reservas = reservas
        self.root = root
        self.root.geometry("500x400")
        self.root.title("Pousada Maré Mansa")
        self.abrir_tela_login()

    def limpar_tela(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def abrir_tela_login(self):
        self.limpar_tela()
        self.root.title("Login - Pousada Maré Mansa")

        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        tk.Label(frame, text="Tela de Login", font=("Arial", 16, "bold")).pack(pady=10)
        tk.Button(frame, text="Voltar", command=self.abrir_tela_gerenciamento).pack(pady=5)

    def abrir_tela_gerenciamento(self):
        self.limpar_tela()
        self.root.title("Pousada Maré Mansa - Menu Principal")

        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        tk.Label(frame, text="Sistema de Gestão da Pousada Maré Mansa", font=("Arial", 14, "bold")).pack(pady=10)

        botoes = [
            ("Gerenciar Agendamentos", self.abrir_agendamentos),
            ("Gerenciar Quartos", self.abrir_quartos),
            ("Fazer Agendamento", self.abrir_agendamentos),
            ("Sair", self.sair)
        ]

        for texto, comando in botoes:
            tk.Button(frame, text=texto, width=30, command=comando).pack(pady=5)

    def abrir_tela_padrao(self, titulo):
        self.limpar_tela()
        self.root.title(f"Pousada Maré Mansa - {titulo}")

        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        tk.Label(frame, text=titulo, font=("Arial", 14, "bold")).pack(pady=10)
        tk.Button(frame, text="Voltar", command=self.abrir_tela_gerenciamento).pack(pady=10)

    def abrir_agendamentos(self):
        self.limpar_tela()
        self.root.title("Pousada Maré Mansa - Cadastro de Agendamento")

        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        tk.Label(frame, text="Cadastro de Agendamento", font=("Arial", 14, "bold")).pack(pady=10)

        # Nome do cliente
        tk.Label(frame, text="Nome do Cliente:").pack()
        nome_entry = tk.Entry(frame, width=30)
        nome_entry.pack(pady=5)

        # ID do quarto
        tk.Label(frame, text="ID do Quarto:").pack()
        quarto_entry = tk.Entry(frame, width=10)
        quarto_entry.pack(pady=5)

        # Seleção de data de entrada
        tk.Label(frame, text="Data de Entrada (DD/MM/AAAA):").pack()
        data_entrada_entry = tk.Entry(frame, width=20)
        data_entrada_entry.pack(pady=5)

        # Seleção de data de saída
        tk.Label(frame, text="Data de Saída (DD/MM/AAAA):").pack()
        data_saida_entry = tk.Entry(frame, width=20)
        data_saida_entry.pack(pady=5)

        def reservar():
            nome = nome_entry.get().strip()
            id_quarto = quarto_entry.get().strip()
            entrada_str = data_entrada_entry.get().strip()
            saida_str = data_saida_entry.get().strip()

            if not nome or not id_quarto or not entrada_str or not saida_str:
                messagebox.showwarning("Campos vazios", "Preencha todos os campos.")
                return

            try:
                data_entrada = datetime.strptime(entrada_str, "%d/%m/%Y").date()
                data_saida = datetime.strptime(saida_str, "%d/%m/%Y").date()
                id_quarto = int(id_quarto)
            except ValueError:
                messagebox.showerror("Erro", "Data ou ID do quarto inválido.")
                return

            cliente = Cliente(nome=nome)  # você pode ajustar para usar um ID real
            quarto = Quarto(numero_quarto=id_quarto)  # idem

            if self.agendamento_controller.existe_agendamento_na_data(data_entrada, quarto):
                messagebox.showerror("Data Ocupada", "⚠️ Este quarto já está reservado para essa data.")
            else:
                self.agendamento_controller.criar_agendamento(data_entrada, data_saida, cliente, quarto)
                messagebox.showinfo("Reserva Confirmada", f"✅ Reserva feita para {nome} no quarto {id_quarto}")
                nome_entry.delete(0, tk.END)
                quarto_entry.delete(0, tk.END)
                data_entrada_entry.delete(0, tk.END)
                data_saida_entry.delete(0, tk.END)

        tk.Button(frame, text="Reservar", command=reservar).pack(pady=10)

        def ver_reservas():
            ags = self.agendamento_controller.listar_agendamentos()
            if not ags:
                messagebox.showinfo("Reservas", "📭 Nenhuma reserva feita.")
            else:
                texto = "Reservas:\n"
                for ag in ags:
                    texto += f"{ag.data_entrada} até {ag.data_saida} -> {ag.cliente.nome} (Quarto {ag.quarto.id})\n"
                messagebox.showinfo("Reservas", texto)

        tk.Button(frame, text="Ver Reservas", command=ver_reservas).pack(pady=5)
        tk.Button(frame, text="Voltar ao Menu", command=self.abrir_tela_gerenciamento).pack(pady=10)

    def abrir_quartos(self):
        self.abrir_tela_padrao("Quartos")

    def sair(self):
        self.root.destroy()

# Execução do programa
if __name__ == "__main__":
    root = tk.Tk()
    app = TelasPousada(root)
    root.mainloop()