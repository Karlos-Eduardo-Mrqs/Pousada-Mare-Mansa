from controllers.banco import Banco

banco = Banco()
banco.conectar()
banco.criar_tabelas()
banco.desconectar()
