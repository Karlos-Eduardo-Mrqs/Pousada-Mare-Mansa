from controllers.banco import Banco
from controllers.telas import TelasPousada
from tkinter import *

# Conectar ao banco
banco = Banco()
banco.conectar()
banco.criar_tabelas()

# Criar janela principal
root = Tk()
telas = TelasPousada(root)

root.mainloop()
