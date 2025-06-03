import tkinter as tk
from tkinter import ttk, messagebox
from views.form_agendamento import Forms_Agendamento
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
        # Topo
        topo = tk.Frame(self.root, bg='#3A7765', height=60)
        topo.pack(side=tk.TOP, fill=tk.X)

        titulo = tk.Label(topo, text="Agendamentos", bg='#3A7765', fg='white',
                          font=("Helvetica", 18, "bold"))
        titulo.pack(pady=10)

        # Campo de pesquisa
        frame_pesquisa = tk.Frame(self.root, bg='#FCEBD5')
        frame_pesquisa.pack(pady=10)

        tk.Label(frame_pesquisa, text="Pesquisar:", bg='#FCEBD5').pack(side=tk.LEFT)
        self.entrada_pesquisa = tk.Entry(frame_pesquisa)
        self.entrada_pesquisa.pack(side=tk.LEFT, padx=5)
        tk.Button(frame_pesquisa, text="Buscar", command=self.buscar_agendamento).pack(side=tk.LEFT)

        # Tabela
        colunas = ("id", "nome", "data_entrada", "data_saida", "quarto", "cpf", "email")
        self.tabela = ttk.Treeview(self.root, columns=colunas, show="headings", height=15)
        for col in colunas:
            self.tabela.heading(col, text=col.replace('_', ' ').capitalize())
            self.tabela.column(col, anchor=tk.CENTER)

        self.tabela.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Botões
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
                ag['id'], ag['nome'], ag['data_entrada'], ag['data_saida'],
                ag['quarto'], ag['cpf'], ag['email']
            ))

    def buscar_agendamento(self):
        termo = self.entrada_pesquisa.get().lower()
        filtrados = [ag for ag in self.dados if termo in ag['nome'].lower()]
        self.atualizar_tabela(filtrados)

    def criar_agendamento(self):
        Forms_Agendamento(self.root, self.conn, self.carregar_dados)

    def editar_agendamento(self):
        item = self.tabela.selection()
        if not item:
            messagebox.showwarning("Atenção", "Selecione um agendamento para editar.")
            return
        valores = self.tabela.item(item[0])["values"]
        dados_editar = {
            'id': valores[0],
            'nome': valores[1],
            'data_entrada': valores[2],
            'data_saida': valores[3],
            'quarto': valores[4],
            'cpf': valores[5],
            'email': valores[6]
        }
        Forms_Agendamento(self.root, self.conn, self.carregar_dados, dados=(
            dados_editar['id'], dados_editar['nome'], dados_editar['data_entrada'],
            dados_editar['data_saida'], dados_editar['cpf'], dados_editar['email'],
            dados_editar['quarto']
        ))

    def deletar_agendamento(self):
        item = self.tabela.selection()
        if not item:
            messagebox.showwarning("Atenção", "Selecione um agendamento para deletar.")
            return
        resposta = messagebox.askyesno("Confirmação", "Tem certeza que deseja cancelar este agendamento?")
        if resposta:
            valores = self.tabela.item(item[0])["values"]
            id_agendamento = valores[0]

            # Deletar no banco
            self.ctr_agendamento.remover_agendamento(int(id_agendamento))

            # Atualiza status do quarto para disponível
            numero_quarto = valores[4]
            self.ctr_quarto.atualizar_status_quarto(True, int(numero_quarto))
            self.carregar_dados()

    def voltar_menu(self):
        self.app.voltar_menu()

# Exemplo de execução do app (com controlador fictício)
if __name__ == "__main__":
    root = tk.Tk()
    TelaAgendamento(root, None, None)
    root.mainloop()
