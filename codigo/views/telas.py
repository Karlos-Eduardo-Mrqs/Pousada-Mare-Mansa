import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# Importações dos controladores e modelos
from controllers.banco import Banco


class TelasPousada:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x400")
        self.root.title("Pousada Maré Mansa")

        # Inicializa o banco e conecta aos controladores
        self.banco = Banco()
        self.banco.conectar()
        self.banco.criar_tabelas()

        self.agendamento_controller = self.banco.control_agendamento
        self.cliente_controller = self.banco.control_cliente
        self.quarto_controller = self.banco.control_quarto

        self.abrir_tela_login()

    def limpar_tela(self):
        """Limpa todos os widgets da tela"""
        for widget in self.root.winfo_children():
            widget.destroy()

    def abrir_tela_login(self):
        """Tela inicial de login (simulada)"""
        self.limpar_tela()
        self.root.title("Login - Pousada Maré Mansa")

        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        tk.Label(frame, text="Tela de Login", font=("Arial", 16, "bold")).pack(pady=10)
        tk.Button(frame, text="Voltar", command=self.abrir_tela_gerenciamento).pack(pady=5)

    def abrir_tela_gerenciamento(self):
        """Menu principal com opções do sistema"""
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
        """Tela genérica com título e botão Voltar"""
        self.limpar_tela()
        self.root.title(f"Pousada Maré Mansa - {titulo}")

        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        tk.Label(frame, text=titulo, font=("Arial", 14, "bold")).pack(pady=10)
        tk.Button(frame, text="Voltar", command=self.abrir_tela_gerenciamento).pack(pady=10)

    def abrir_agendamentos(self):
        """Tela de cadastro de agendamento"""
        self.limpar_tela()
        self.root.title("Pousada Maré Mansa - Cadastro de Agendamento")

        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        tk.Label(frame, text="Cadastro de Agendamento", font=("Arial", 14, "bold")).pack(pady=10)

        # CPF do cliente
        tk.Label(frame, text="CPF do Cliente:").pack()
        cpf_entry = tk.Entry(frame, width=30)
        cpf_entry.pack(pady=5)

        # Número do quarto
        tk.Label(frame, text="Número do Quarto:").pack()
        quarto_entry = tk.Entry(frame, width=10)
        quarto_entry.pack(pady=5)

        # Data de entrada
        tk.Label(frame, text="Data de Entrada (DD/MM/AAAA):").pack()
        data_entrada_entry = tk.Entry(frame, width=20)
        data_entrada_entry.pack(pady=5)

        # Data de saída
        tk.Label(frame, text="Data de Saída (DD/MM/AAAA):").pack()
        data_saida_entry = tk.Entry(frame, width=20)
        data_saida_entry.pack(pady=5)

        def reservar():
            cpf = cpf_entry.get().strip()
            numero_quarto = quarto_entry.get().strip()
            entrada_str = data_entrada_entry.get().strip()
            saida_str = data_saida_entry.get().strip()

            if not cpf or not numero_quarto or not entrada_str or not saida_str:
                messagebox.showwarning("Campos vazios", "Preencha todos os campos.")
                return

            try:
                data_entrada = datetime.strptime(entrada_str, "%d/%m/%Y").date()
                data_saida = datetime.strptime(saida_str, "%d/%m/%Y").date()
                numero_quarto = int(numero_quarto)
            except ValueError:
                messagebox.showerror("Erro", "Data ou número do quarto inválido.")
                return

            # Busca cliente no banco
            clientes = self.cliente_controller.listar_clientes()
            cliente_encontrado = next((c for c in clientes if c["cpf"] == cpf), None)
            if not cliente_encontrado:
                messagebox.showerror("Erro", "Cliente não encontrado.")
                return

            # Busca quarto no banco
            quartos = self.quarto_controller.listar_quartos()
            quarto_encontrado = next((q for q in quartos if q["numero"] == numero_quarto), None)
            if not quarto_encontrado:
                messagebox.showerror("Erro", "Quarto não encontrado.")
                return

            # Verifica disponibilidade
            if self.agendamento_controller.existe_agendamento_na_data(data_entrada, numero_quarto):
                messagebox.showerror("Data Ocupada", "⚠️ Este quarto já está reservado para essa data.")
            else:
                self.agendamento_controller.adicionar_agendamento(
                    data_entrada, data_saida, cpf, numero_quarto
                )
                messagebox.showinfo("Reserva Confirmada",
                                    f"✅ Reserva feita para {cliente_encontrado['nome']} no quarto {numero_quarto}")
                cpf_entry.delete(0, tk.END)
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
                    texto += f"{ag['data_entrada']} até {ag['data_saida']} -> {ag['cpf']} (Quarto {ag['numero_quarto']})\n"
                messagebox.showinfo("Reservas", texto)

        tk.Button(frame, text="Ver Reservas", command=ver_reservas).pack(pady=5)
        tk.Button(frame, text="Voltar ao Menu", command=self.abrir_tela_gerenciamento).pack(pady=10)

    def abrir_quartos(self):
        """Tela temporária para gerenciar quartos"""
        self.abrir_tela_padrao("Quartos")

    def sair(self):
        """Fecha o aplicativo"""
        self.banco.desconectar()
        self.root.destroy()


# Se você estiver rodando diretamente por esse arquivo, use:
if __name__ == "__main__":
    root = tk.Tk()
    app = TelasPousada(root)
    root.mainloop()