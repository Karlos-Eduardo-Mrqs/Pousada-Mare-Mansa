import tkinter as tk
from tkinter import ttk, messagebox
from views.form_agendamento import FormsAgendamento
from controllers.control_agendamento import Control_Agendamento
from controllers.control_quarto import Control_Quarto

class TelaAgendamento:
    def __init__(self, root, app, conn):
        self.root = root
        self.app = app
        self.conn = conn

        self.ctr_agendamento = Control_Agendamento(self.conn)
        self.ctr_quarto = Control_Quarto(self.conn)

        self.root.title("Agendamentos - Pousada Maré Mansa")
        self.root.geometry("800x500")
        self.root.configure(bg='#FCEBD5')

        self.dados = []
        self.criar_interface()
        self.carregar_dados()

    def criar_interface(self):
        topo = tk.Frame(self.root, bg='#3A7765', height=60)
        topo.pack(side=tk.TOP, fill=tk.X)

        titulo = tk.Label(topo, text="Agendamentos", bg='#3A7765', fg='white',
                          font=("Helvetica", 18, "bold"))
        titulo.pack(pady=10)

        frame_pesquisa = tk.Frame(self.root, bg='#FCEBD5')
        frame_pesquisa.pack(pady=10)

        tk.Label(frame_pesquisa, text="Pesquisar:", bg='#FCEBD5').pack(side=tk.LEFT)
        self.entrada_pesquisa = tk.Entry(frame_pesquisa)
        self.entrada_pesquisa.pack(side=tk.LEFT, padx=5)
        tk.Button(frame_pesquisa, text="Buscar", command=self.buscar_agendamento).pack(side=tk.LEFT)

        colunas = ("nome", "email", "data_entrada", "data_saida", "quarto_id", "tipo", "preco")
        self.tabela = ttk.Treeview(self.root, columns=colunas, show="headings", height=15)

        nomes_colunas = {
            "nome": "Nome",
            "email": "Email",
            "data_entrada": "Data de Entrada",
            "data_saida": "Data de Saída",
            "quarto_id": "Quarto",
            "tipo": "Tipo",
            "preco": "Preço (R$)"
        }

        for col in colunas:
            self.tabela.heading(col, text=nomes_colunas[col])
            self.tabela.column(col, anchor=tk.CENTER)

        self.tabela.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        frame_botoes = tk.Frame(self.root, bg='#FCEBD5')
        frame_botoes.pack(pady=10)

        tk.Button(frame_botoes, text="Criar", command=self.criar_agendamento).pack(side=tk.LEFT, padx=10)
        tk.Button(frame_botoes, text="Editar", command=self.editar_agendamento).pack(side=tk.LEFT, padx=10)
        tk.Button(frame_botoes, text="Deletar", command=self.deletar_agendamento).pack(side=tk.LEFT, padx=10)
        tk.Button(frame_botoes, text="Voltar ao Menu", bg="#D9B08C", command=self.voltar_menu).pack(side=tk.LEFT, padx=10)

    def carregar_dados(self):
        self.dados = self.ctr_agendamento.listar_agendamentos()
        self.atualizar_tabela(self.dados)

    def atualizar_tabela(self, dados):
        for i in self.tabela.get_children():
            self.tabela.delete(i)
        for ag in dados:
            self.tabela.insert('', tk.END, values=(
                ag['nome'], ag['email'], ag['data_entrada'], ag['data_saida'],
                ag['quarto_id'], ag['tipo'], f"{ag['preco']:.2f}"
            ))

    def buscar_agendamento(self):
        termo = self.entrada_pesquisa.get().lower()
        filtrados = [ag for ag in self.dados if termo in ag['nome'].lower()]
        self.atualizar_tabela(filtrados)

    def criar_agendamento(self):
        FormsAgendamento(self.root, self.conn)
        self.root.wait_window()  # Espera o formulário fechar
        self.carregar_dados()

    def editar_agendamento(self):
        item = self.tabela.selection()
        if not item:
            messagebox.showwarning("Atenção", "Selecione um agendamento para editar.")
            return
        valores = self.tabela.item(item[0])["values"]

        agendamento = next((ag for ag in self.dados if
                            ag['nome'] == valores[0] and ag['email'] == valores[1]), None)

        if agendamento:
            FormsAgendamento(
                self.root,
                self.conn,
                (
                    agendamento['id'],
                    agendamento['data_entrada'],
                    agendamento['data_saida'],
                    agendamento['cliente_cpf'],
                    agendamento['quarto_id']
                )
            )
            self.root.wait_window()
            self.carregar_dados()

    def deletar_agendamento(self):
        item = self.tabela.selection()
        if not item:
            messagebox.showwarning("Atenção", "Selecione um agendamento para deletar.")
            return
        valores = self.tabela.item(item[0])["values"]
        agendamento = next((ag for ag in self.dados if
                            ag['nome'] == valores[0] and ag['email'] == valores[1]), None)
        if agendamento:
            confirm = messagebox.askyesno("Confirmação", "Tem certeza que deseja deletar este agendamento?")
            if confirm:
                self.ctr_agendamento.remover_agendamento(agendamento['id'])
                self.carregar_dados()

    def voltar_menu(self):
        self.root.destroy()
        self.app.mostrar_menu_principal()
