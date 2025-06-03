import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from controllers.control_cliente import Control_Cliente
from controllers.control_tipo import Control_Tipo
from controllers.control_quarto import Control_Quarto
from controllers.control_agendamento import Control_Agendamento

class Forms_Agendamento:
    def __init__(self, parent, conn, callback, dados=None):
        self.parent = parent
        self.conn = conn
        self.callback = callback
        self.dados = dados  # se passado, é edição; se None, é criação

        self.ctr_quarto = Control_Quarto(self.conn)
        self.ctr_cliente = Control_Cliente(self.conn)
        self.ctr_tipo = Control_Tipo(self.conn)
        self.ctr_agendamento = Control_Agendamento(self.conn)

        self.janela = tk.Toplevel(self.parent)
        self.janela.title("Agendamento")
        self.janela.geometry("350x300")
        self.janela.configure(bg='#FCEBD5')
        self.janela.grab_set()  # bloqueia interação com janela pai

        self._criar_widgets()
        if self.dados:
            self._carregar_dados()

    def _criar_widgets(self):
        # Labels e entradas
        tk.Label(self.janela, text="CPF:", bg='#FCEBD5').grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.entry_cpf = tk.Entry(self.janela)
        self.entry_cpf.grid(row=0, column=1, padx=5, pady=5)
        self.entry_cpf.bind("<FocusOut>", self.buscar_cliente)

        tk.Label(self.janela, text="Nome:", bg='#FCEBD5').grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.entry_nome = tk.Entry(self.janela)
        self.entry_nome.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.janela, text="E-mail:", bg='#FCEBD5').grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.entry_email = tk.Entry(self.janela)
        self.entry_email.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.janela, text="Data entrada:", bg='#FCEBD5').grid(row=3, column=0, padx=5, pady=5, sticky='e')
        self.entry_check_in = DateEntry(self.janela, date_pattern='dd/mm/yyyy')
        self.entry_check_in.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.janela, text="Data saída:", bg='#FCEBD5').grid(row=4, column=0, padx=5, pady=5, sticky='e')
        self.entry_check_out = DateEntry(self.janela, date_pattern='dd/mm/yyyy')
        self.entry_check_out.grid(row=4, column=1, padx=5, pady=5)

        # Lista quartos disponíveis
        lista = self.ctr_quarto.listar_quartos()
        quartos_disponiveis = [str(row['numero']) for row in lista if row['disponibilidade']]
        tk.Label(self.janela, text="Quarto:", bg='#FCEBD5').grid(row=5, column=0, padx=5, pady=5, sticky='e')
        self.entry_quarto = ttk.Combobox(self.janela, values=quartos_disponiveis)
        self.entry_quarto.grid(row=5, column=1, padx=5, pady=5)

        # Botões
        btn_salvar = tk.Button(self.janela, text="Salvar", command=self.btn_salvar)
        btn_salvar.grid(row=6, column=0, padx=5, pady=15, sticky='e')

        btn_cancelar = tk.Button(self.janela, text="Cancelar", command=self.janela.destroy)
        btn_cancelar.grid(row=6, column=1, padx=5, pady=15, sticky='w')

    def _carregar_dados(self):
        if not self.dados:
            return  # ou lançar erro se isso nunca deveria acontecer

        id_agendamento = self.dados[0]
        nome = self.dados[1]
        data_entrada = self.dados[2]
        data_saida = self.dados[3]
        cpf = self.dados[4]
        email = self.dados[5]
        quarto = str(self.dados[6])

        self.entry_cpf.insert(0, cpf)
        self.entry_nome.insert(0, nome)
        self.entry_email.insert(0, email)
        self.entry_check_in.set_date(data_entrada)
        self.entry_check_out.set_date(data_saida)
        self.entry_quarto.set(quarto)

    def buscar_cliente(self, event):
        cpf = self.entry_cpf.get()
        if cpf:
            cliente = self.ctr_cliente.buscar_cliente_por_cpf(cpf)
            if cliente:
                self.entry_nome.delete(0, tk.END)
                self.entry_nome.insert(0, cliente["nome"])
                self.entry_email.delete(0, tk.END)
                self.entry_email.insert(0, cliente["email"])
            else:
                messagebox.showinfo("Info", "Cliente não encontrado.")

    def btn_salvar(self):
        cpf = self.entry_cpf.get()
        nome = self.entry_nome.get()
        email = self.entry_email.get()
        data_entrada = self.entry_check_in.get()
        data_saida = self.entry_check_out.get()
        quarto_str = self.entry_quarto.get()

        # Validar campos
        if not all([cpf, nome, email, data_entrada, data_saida, quarto_str]):
            messagebox.showwarning("Aviso", "Preencha todos os campos.")
            return

        try:
            numero_quarto = int(quarto_str)
        except ValueError:
            messagebox.showwarning("Aviso", "Número do quarto inválido.")
            return

        # Criar cliente se não existir
        cliente = self.ctr_cliente.buscar_cliente_por_cpf(cpf)
        if cliente is None:
            self.ctr_cliente.criar_tabela()
            self.ctr_cliente.adicionar_cliente(cpf, nome, email)

        # Criar ou atualizar agendamento
        self.ctr_agendamento.criar_tabela()

        if self.dados:  # edição
            id_agendamento = self.dados[0]
            self.ctr_agendamento.atualizar_agendamento(id_agendamento, data_entrada, data_saida, cpf, int(numero_quarto))
        else:  # criação
            self.ctr_agendamento.adicionar_agendamento(data_entrada, data_saida, cpf, numero_quarto)

        # Atualiza status do quarto (marca como indisponível)
        self.ctr_quarto.atualizar_status_quarto(False, numero_quarto)

        messagebox.showinfo("Sucesso", "Agendamento salvo com sucesso!")

        # Atualiza a lista na tela principal via callback
        self.callback()

        self.janela.destroy()
