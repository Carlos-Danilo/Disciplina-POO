# contato_dao.py
import json
from Contato import Contato

class ContatoDAO:
    def __init__(self):
        self.contatos = []

    def adicionar(self, contato):
        self.contatos.append(contato)

    def listar(self):
        return self.contatos

    def buscar_por_id(self, id):
        return next((c for c in self.contatos if c.id == id), None)

    def atualizar(self, id, nome, email, telefone, nascimento):
        contato = self.buscar_por_id(id)
        if contato:
            contato.nome = nome
            contato.email = email
            contato.telefone = telefone
            contato.nascimento = nascimento
            return True
        return False

    def remover(self, id):
        self.contatos = [c for c in self.contatos if c.id != id]

    def pesquisar_por_iniciais(self, iniciais):
        return [c for c in self.contatos if c.nome.lower().startswith(iniciais.lower())]

    def aniversariantes_do_mes(self, mes):
        return [c for c in self.contatos if c.get_mes_nascimento() == mes]

    def salvar_em_arquivo(self, caminho):
        with open(caminho, 'w', encoding='utf-8') as f:
            json.dump([c.__dict__ for c in self.contatos], f, ensure_ascii=False, indent=4)

    def carregar_de_arquivo(self, caminho):
        try:
            with open(caminho, 'r', encoding='utf-8') as f:
                dados = json.load(f)
                self.contatos = [Contato(**d) for d in dados]
        except FileNotFoundError:
            self.contatos = []
