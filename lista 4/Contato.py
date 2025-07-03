class Contato:
    def __init__(self, i, n, e, f):
        self.__id = i
        self.__nome = n
        self.__email = e
        self.__fone = f
    def get_nome(self):
        return self.__nome
    def get_ID(self):
        return self.__id    
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"
        
class ContatoUI:
    __contatos = []

    @classmethod
    def main(cls):
        op = 0
        while op != 6:
            op = ContatoUI.menu()
            if op == 1: ContatoUI.inserir()
            if op == 2: ContatoUI.listar()
            if op == 3: ContatoUI.atualizar()
            if op == 4: ContatoUI.excluir()
            if op == 5: ContatoUI.pesquisar()

    @classmethod
    def menu(cls):
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 5-Pesquisar, 6-Fim")
        return int(input("Informe uma opção: "))
    
    @classmethod
    def inserir(cls):
        id = int(input("Informe o id do contato: "))
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o fone: ")
        c = Contato(id, nome, email, fone)
        cls.__contatos.append(c)

    @classmethod
    def listar(cls):
        for c in cls.__contatos:
            print(c)

    @classmethod
    def atualizar(cls):
        if len(cls.__contatos) == 0:
            raise ValueError("Lista sem contatos.")
        id = int(input("Digite o ID do contato:\n"))
        for c in cls.__contatos:
            if c.get_ID() == id:
                nome = input("Digite o novo nome: ")
                email = input("Digite o novo E-Mail: ")
                fone = input("Digite o novo telefone: ")
                cls.__contatos[cls.__contatos.index(c)] = Contato(id, nome, email, fone)

    @classmethod
    def excluir(cls):
        id = int(input("Informe o id do contato a ser excluído: "))
        for c in cls.__contatos:
            if c.get_nome() == id:
                cls.__contatos.remove(c)
                print("Contato excluído com sucesso.")
                break
        else:
            print("Contato não encontrado.")

    @classmethod
    def pesquisar(cls):
        nome = input("Informe o nome do contato: ")
        for c in cls.__contatos:
            if c.get_nome().startswith(nome):
                print(c)

ContatoUI.main()