# view.py
from ContatoDAO import ContatoDAO
from Contato import Contato

class View:
    def __init__(self):
        self.dao = ContatoDAO()
        self.proximo_id = 1

    def inserir(self, nome, email, telefone, nascimento):
        contato = Contato(self.proximo_id, nome, email, telefone, nascimento)
        self.dao.adicionar(contato)
        self.proximo_id += 1

    def listar(self):
        return self.dao.listar()

    def buscar_por_id(self, id):
        return self.dao.buscar_por_id(id)

    def atualizar(self, id, nome, email, telefone, nascimento):
        return self.dao.atualizar(id, nome, email, telefone, nascimento)

    def excluir(self, id):
        self.dao.remover(id)

    def pesquisar_iniciais(self, iniciais):
        return self.dao.pesquisar_por_iniciais(iniciais)

    def aniversariantes_mes(self, mes):
        return self.dao.aniversariantes_do_mes(mes)

    def salvar(self, caminho):
        self.dao.salvar_em_arquivo(caminho)

    def abrir(self, caminho):
        self.dao.carregar_de_arquivo(caminho)
        if self.dao.contatos:
            self.proximo_id = max(c.id for c in self.dao.contatos) + 1
        else:
            self.proximo_id = 1
