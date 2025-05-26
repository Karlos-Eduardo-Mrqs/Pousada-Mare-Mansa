from controllers.banco import Banco
from controllers.telas import TelasPython
from tkinter import *

# Conectar ao banco
banco = Banco()
banco.conectar()
banco.criar_tabelas()

# Iniciar interface gráfica
root = Tk()
tela = TelasPython(root)  # passando a conexão para uso nas telas
root.mainloop()

# Desconectar banco ao encerrar a aplicação
banco.desconectar()
