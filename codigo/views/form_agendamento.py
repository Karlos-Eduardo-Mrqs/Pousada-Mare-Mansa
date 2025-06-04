import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import datetime

from controllers.control_cliente import Control_Cliente
from controllers.control_tipo import Control_Tipo
from controllers.control_quarto import Control_Quarto
from controllers.control_agendamento import Control_Agendamento

class FormsAgendamento:
    def __init__(self, parent, conn, dados_iniciais=None):
        self.parent = parent
        self.conn = conn
        self.dados_iniciais = dados_iniciais  # se passado, é edição

        self.ctr_cliente = Control_Cliente(self.conn)
        self.ctr_quarto = Control_Quarto(self.conn)
        self.ctr_tipo = Control_Tipo(self.conn)
        self.ctr_agendamento = Control_Agendamento(self.conn)

        self.janela = tk.Toplevel(self.parent)
        self.janela.title("Agendamento")
        self.janela.geometry("350x300")
        self.janela.configure(bg="#FCEBD5")
        self.janela.grab_set()

        self._criar_widgets()
        if self.dados_iniciais:
            self._preencher_dados()

    def _criar_widgets(self):
        # CPF
        tk.Label(self.janela, text="CPF:", bg="#FCEBD5").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_cpf = tk.Entry(self.janela)
        self.entry_cpf.grid(row=0, column=1, padx=5, pady=5)
        self.entry_cpf.bind("<FocusOut>", self._buscar_cliente)

        # Nome
        tk.Label(self.janela, text="Nome:", bg="#FCEBD5").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_nome = tk.Entry(self.janela)
        self.entry_nome.grid(row=1, column=1, padx=5, pady=5)

        # Email
        tk.Label(self.janela, text="E-mail:", bg="#FCEBD5").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_email = tk.Entry(self.janela)
        self.entry_email.grid(row=2, column=1, padx=5, pady=5)

        # Data de entrada
        tk.Label(self.janela, text="Data entrada:", bg="#FCEBD5").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.entry_check_in = DateEntry(self.janela, date_pattern="dd/mm/yyyy")
        self.entry_check_in.grid(row=3, column=1, padx=5, pady=5)

        # Data de saída
        tk.Label(self.janela, text="Data saída:", bg="#FCEBD5").grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.entry_check_out = DateEntry(self.janela, date_pattern="dd/mm/yyyy")
        self.entry_check_out.grid(row=4, column=1, padx=5, pady=5)

        # Quarto
        tk.Label(self.janela, text="Quarto:", bg="#FCEBD5").grid(row=5, column=0, padx=5, pady=5, sticky="e")
        quartos = self.ctr_quarto.listar_quartos()
        quartos_disponiveis = [str(q["numero"]) for q in quartos if q.get("disponibilidade", True)]
        self.entry_quarto = ttk.Combobox(self.janela, values=quartos_disponiveis, state="readonly")
        self.entry_quarto.grid(row=5, column=1, padx=5, pady=5)

        # Botões
        tk.Button(self.janela, text="Salvar", command=self._salvar).grid(row=6, column=0, padx=5, pady=15, sticky="e")
        tk.Button(self.janela, text="Cancelar", command=self.janela.destroy).grid(row=6, column=1, padx=5, pady=15, sticky="w")

    def _preencher_dados(self):
        if not self.dados_iniciais:
            return
        id_ag, nome, entrada, saida, cpf, email, numero_quarto = self.dados_iniciais
        self.entry_cpf.insert(0, cpf)
        self.entry_nome.insert(0, nome)
        self.entry_email.insert(0, email)
        self.entry_check_in.set_date(datetime.strptime(entrada, "%Y-%m-%d"))
        self.entry_check_out.set_date(datetime.strptime(saida, "%Y-%m-%d"))
        self.entry_quarto.set(str(numero_quarto))

    def _buscar_cliente(self, event=None):
        cpf = self.entry_cpf.get().strip()
        if cpf:
            cliente = self.ctr_cliente.buscar_cliente_por_cpf(cpf)
            if cliente:
                self.entry_nome.delete(0, tk.END)
                self.entry_nome.insert(0, cliente["nome"])
                self.entry_email.delete(0, tk.END)
                self.entry_email.insert(0, cliente["email"])
            else:
                messagebox.showinfo("Info", "Cliente não encontrado.")

    def _salvar(self):
        cpf = self.entry_cpf.get().strip()
        nome = self.entry_nome.get().strip()
        email = self.entry_email.get().strip()
        entrada = self.entry_check_in.get_date()
        saida = self.entry_check_out.get_date()
        quarto_str = self.entry_quarto.get()

        if not all([cpf, nome, email, entrada, saida, quarto_str]):
            messagebox.showwarning("Aviso", "Preencha todos os campos.")
            return

        if saida <= entrada:
            messagebox.showwarning("Aviso", "Data de saída deve ser posterior à data de entrada.")
            return

        try:
            numero_quarto = int(quarto_str)
        except ValueError:
            messagebox.showwarning("Aviso", "Número de quarto inválido.")
            return

        # Garantir existência das tabelas
        self.ctr_cliente.criar_tabela()
        self.ctr_quarto.criar_tabela()
        self.ctr_agendamento.criar_tabela()

        # Adicionar cliente caso não exista
        if not self.ctr_cliente.buscar_cliente_por_cpf(cpf):
            self.ctr_cliente.adicionar_cliente(cpf, nome, email)

        # Valida disponibilidade do quarto
        if not self.dados_iniciais or (self.dados_iniciais and int(self.dados_iniciais[6]) != numero_quarto):
            quarto_info = self.ctr_quarto.buscar_quarto_por_numero(numero_quarto)
            if not quarto_info or not quarto_info.get("disponibilidade", True):
                messagebox.showwarning("Aviso", "Quarto não está disponível.")
                return

        if self.dados_iniciais:
            id_ag = self.dados_iniciais[0]
            self.ctr_agendamento.atualizar_agendamento(id_ag, entrada.strftime("%Y-%m-%d"), saida.strftime("%Y-%m-%d"), cpf, numero_quarto)
        else:
            self.ctr_agendamento.adicionar_agendamento(entrada.strftime("%Y-%m-%d"), saida.strftime("%Y-%m-%d"), cpf, numero_quarto)

        # Atualizar status do quarto
        self.ctr_quarto.atualizar_status_quarto(False, numero_quarto)

        # Liberar quarto anterior se alterado
        if self.dados_iniciais and int(self.dados_iniciais[6]) != numero_quarto:
            self.ctr_quarto.atualizar_status_quarto(True, int(self.dados_iniciais[6]))

        messagebox.showinfo("Sucesso", "Agendamento salvo com sucesso!")
        self.janela.destroy()
