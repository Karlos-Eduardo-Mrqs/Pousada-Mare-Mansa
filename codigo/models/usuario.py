from dataclasses import dataclass

@dataclass
class Usuario:
    def __init__(self, id:int, nome:str, email:str, senha:str):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha