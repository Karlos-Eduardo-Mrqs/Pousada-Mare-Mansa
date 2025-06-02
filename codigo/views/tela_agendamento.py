import tkinter as tk
from tkinter import ttk, messagebox
from .forms_agendamento import Forms_Agendamento

class TelaAgendamento:
    def __init__(self, root, app):
        self.root = root        # pega a janela raiz do controlador
        self.app = app          # controlador para voltar ao menu
        self.root.title("Agendamentos - Pousada Maré Mansa")
        self.root.geometry("800x500")
        self.root.configure(bg='#FCEBD5')
        self.dados = []  # Simulação de banco

        self.criar_interface()

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
        colunas = ("id", "nome", "data", "quarto")
        self.tabela = ttk.Treeview(self.root, columns=colunas, show="headings", height=15)
        for col in colunas:
            self.tabela.heading(col, text=col.capitalize())
            self.tabela.column(col, anchor=tk.CENTER)

        self.tabela.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Botões
        frame_botoes = tk.Frame(self.root, bg='#FCEBD5')
        frame_botoes.pack(pady=10)

        tk.Button(frame_botoes, text="Criar", command=self.criar_agendamento).pack(side=tk.LEFT, padx=10)
        tk.Button(frame_botoes, text="Editar", command=self.editar_agendamento).pack(side=tk.LEFT, padx=10)
        tk.Button(frame_botoes, text="Deletar", command=self.deletar_agendamento).pack(side=tk.LEFT, padx=10)
        tk.Button(frame_botoes, text="Voltar ao Menu", bg="#D9B08C", command=self.voltar_menu).pack(side=tk.LEFT, padx=10)

    def buscar_agendamento(self):
        termo = self.entrada_pesquisa.get().lower()
        for i in self.tabela.get_children():
            self.tabela.delete(i)
        for dado in self.dados:
            if termo in dado['nome'].lower():
                self.tabela.insert('', tk.END, values=(dado['id'], dado['nome'], dado['data'], dado['quarto']))

    def criar_agendamento(self):
        Forms_Agendamento(self.root)

    def editar_agendamento(self):
        item = self.tabela.selection()
        if not item:
            messagebox.showwarning("Atenção", "Selecione um agendamento para editar.")
            return
        valores = self.tabela.item(item[0])["values"]  # Usar item[0] aqui
        self.abrir_janela_agendamento("Editar", valores)

    def deletar_agendamento(self):
        item = self.tabela.selection()
        if not item:
            messagebox.showwarning("Atenção", "Selecione um agendamento para deletar.")
            return
        resposta = messagebox.askyesno("Confirmação", "Tem certeza que deseja cancelar este agendamento?")
        if resposta:
            valores = self.tabela.item(item[0])["values"]  # Usar item[0] aqui
            self.dados = [d for d in self.dados if d['id'] != valores[0]]
            self.buscar_agendamento()

    def abrir_janela_agendamento(self, modo, valores=None):
        janela = tk.Toplevel(self.root)
        janela.title(f"{modo} Agendamento")
        janela.geometry("300x200")
        janela.configure(bg='#FCEBD5')

        campos = ['Nome', 'Data', 'Quarto']
        entradas = {}

        for i, campo in enumerate(campos):
            tk.Label(janela, text=campo, bg='#FCEBD5').grid(row=i, column=0, pady=5, padx=5)
            entrada = tk.Entry(janela)
            entrada.grid(row=i, column=1, pady=5, padx=5)
            entradas[campo.lower()] = entrada

        if modo == "Editar" and valores:
            entradas['nome'].insert(0, valores[1])
            entradas['data'].insert(0, valores[2])
            entradas['quarto'].insert(0, valores[3])

        def salvar():
            novo = {
                'id': valores[0] if valores else len(self.dados) + 1,
                'nome': entradas['nome'].get(),
                'data': entradas['data'].get(),
                'quarto': entradas['quarto'].get()
            }
            if modo == "Criar":
                self.dados.append(novo)
            else:
                for i, d in enumerate(self.dados):
                    if d['id'] == novo['id']:
                        self.dados[i] = novo
            self.buscar_agendamento()
            janela.destroy()

        tk.Button(janela, text="Salvar", command=salvar).grid(row=4, columnspan=2, pady=10)

    def voltar_menu(self):
        self.app.voltar_menu()

# Exemplo de execução do app (com controlador fictício)
if __name__ == "__main__":
    root = tk.Tk()
    TelaAgendamento(root, None)
    root.mainloop()