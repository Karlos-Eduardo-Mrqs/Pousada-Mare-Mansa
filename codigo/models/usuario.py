from dataclasses import dataclass

@dataclass
class Usuario:
    def init(self, id, nome, email, senha):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
