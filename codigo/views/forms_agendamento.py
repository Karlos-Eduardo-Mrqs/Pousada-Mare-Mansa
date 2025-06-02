import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from controllers.control_cliente import Control_Cliente
from controllers.control_tipo import Control_Tipo
# from controllers.control_quarto import Control_Quarto
from controllers.control_agendamento import Control_Agendamento

class Forms_Agendamento:
    def __init__(self,conn):
        self.conn = conn
        self.ctr_quarto = Control_Quarto(self.conn)
        self.ctr_cliente = Control_Cliente(self.conn)
        self.ctr_tipo = Control_Tipo(self.conn)
        self.ctr_agendamento = Control_Agendamento(self.conn)

        # Criar as tabelas uma vez aqui
        self.ctr_cliente.criar_tabela()
        self.ctr_agendamento.criar_tabela()
        self.ctr_quarto.criar_tabela()
        self.ctr_tipo.criar_tabela()

        self.janela = tk.Tk()
        self.janela.title("Agendamento")

        label_cpf = tk.Label(self.janela, text="CPF:")
        self.entry_cpf = tk.Entry(self.janela)
        self.entry_cpf.bind("<FocusOut>", self.buscar_cliente)

        label_nome = tk.Label(self.janela, text="Nome:")
        self.entry_nome = tk.Entry(self.janela)

        label_email = tk.Label(self.janela, text="E-mail:")
        self.entry_email = tk.Entry(self.janela)

        label_check_in = tk.Label(self.janela, text="Data entrada:")
        self.entry_check_in = DateEntry(self.janela, date_pattern='dd/mm/yyyy')

        label_check_out = tk.Label(self.janela, text="Data saída:")
        self.entry_check_out = DateEntry(self.janela, date_pattern='dd/mm/yyyy')

        lista = self.ctr_quarto.listar_quartos()
        quartos_disponiveis = []
        for quarto in lista:
            if quarto.disponibilidade == True:
                quartos_disponiveis.append(quarto.numero_quarto)

        label_quarto = tk.Label(self.janela, text="Quarto:")
        self.entry_quarto = ttk.Combobox(self.janela, values=quartos_disponiveis)

        btn_salvar = tk.Button(self.janela, text="Salvar", command=self.btn_cadastrar)
        btn_cancelar = tk.Button(self.janela, text="Cancelar", command=self.btn_sair)

        label_cpf.grid(row=0, column=0, padx=5, pady=5)
        self.entry_cpf.grid(row=0, column=1, padx=5, pady=5)

        label_nome.grid(row=1, column=0, padx=5, pady=5)
        self.entry_nome.grid(row=1, column=1, padx=5, pady=5)

        label_email.grid(row=2, column=0, padx=5, pady=5)
        self.entry_email.grid(row=2, column=1, padx=5, pady=5)

        label_check_in.grid(row=3, column=0, padx=5, pady=5)
        self.entry_check_in.grid(row=3, column=1, padx=5, pady=5)

        label_check_out.grid(row=4, column=0, padx=5, pady=5)
        self.entry_check_out.grid(row=4, column=1, padx=5, pady=5)

        label_quarto.grid(row=5, column=0, padx=5, pady=5)
        self.entry_quarto.grid(row=5, column=1, padx=5, pady=5)

        btn_salvar.grid(row=6, column=0, padx=5, pady=5, sticky="e")
        btn_cancelar.grid(row=6, column=1, padx=5, pady=5, sticky="w")

        self.janela.mainloop()

    def buscar_cliente(self, event):
        cpf = self.entry_cpf.get()

        if cpf:
            cliente = self.ctr_cliente.buscar_cliente_por_cpf(cpf)
            if cliente:
                self.entry_nome.delete(0, tk.END)
                self.entry_nome.insert(0, cliente["nome"])

                self.entry_email.delete(0, tk.END)
                self.entry_email.insert(0, cliente["nome"])
            else:
                self.entry_nome.delete(0, tk.END)
                self.entry_email.delete(0, tk.END)
                print("Cliente não encontrado.")

    def btn_cadastrar(self):
        cpf = self.entry_cpf.get()
        nome = self.entry_nome.get()
        email = self.entry_email.get()
        check_in = self.entry_check_in.get()
        check_out = self.entry_check_out.get()
        quarto_str = self.entry_quarto.get()

        if not (cpf and nome and email and check_in and check_out and quarto_str):
            print("Por favor, preencha todos os campos.")
            return

        try:
            numero_quarto = int(quarto_str)
        except ValueError:
            print("Número do quarto inválido.")
            return

        # cadastrar cliente se não existir
        cliente = self.ctr_cliente.buscar_cliente_por_cpf(cpf)
        if cliente is None:
            self.ctr_cliente.adicionar_cliente(cpf, nome, email)
            print("Novo cliente cadastrado")
        else:
            print("Cliente já cadastrado")

        # cadastrar agendamento
        self.ctr_agendamento.adicionar_agendamento(check_in, check_out, cpf, numero_quarto)
        print("Agendamento feito com sucesso!")

        # atualizar status do quarto
        self.ctr_quarto.atualizar_status_quarto(False, numero_quarto)

        self.janela.destroy()

    def btn_sair(self):
        self.janela.destroy()


if __name__ == "__main__":
    Forms_Agendamento()