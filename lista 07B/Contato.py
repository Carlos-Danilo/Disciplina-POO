# contato.py
from datetime import datetime

class Contato:
    def __init__(self, id, nome, email, telefone, nascimento):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.nascimento = nascimento  # formato: "dd/mm/aaaa"

    def __str__(self):
        return (f"ID: {self.id}\nNome: {self.nome}\nEmail: {self.email}\n"
                f"Telefone: {self.telefone}\nNascimento: {self.nascimento}")

    def get_mes_nascimento(self):
        try:
            return int(self.nascimento.split("/")[1])
        except:
            return -1
