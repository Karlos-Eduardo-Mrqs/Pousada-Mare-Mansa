from controllers.banco import Banco
from controllers.telas import TelasPousada
from tkinter import *

# Conectar ao banco
banco = Banco()
banco.conectar()
banco.criar_tabelas()
<<<<<<< Updated upstream

# Criar janela principal
root = Tk()
telas = TelasPousada(root)

root.mainloop()
=======
banco.desconectar()

root = Tk()
telas = TelasPousada(root)

<<<<<<< Updated upstream
<<<<<<< Updated upstream
root.mainloop()
>>>>>>> Stashed changes
=======
root.mainloop()
>>>>>>> Stashed changes
=======
root.mainloop()
>>>>>>> Stashed changes
