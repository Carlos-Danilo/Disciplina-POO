from datetime import datetime

class Contato:
    def __init__(self, id: int, nome: str, email: str, telefone: str, nascimento: str):
        # Construtor da classe, inicializa os dados do contato
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone
        self.__nascimento = datetime.strptime(nascimento, "%d-%m-%Y").date()  # Formato da data corrigido

    def get_id(self) -> int:
        return self.__id

    def get_nome(self) -> str:
        return self.__nome

    def get_email(self) -> str:
        return self.__email

    def get_telefone(self) -> str:
        return self.__telefone

    def get_nascimento(self):
        return self.__nascimento

    def set_nome(self, nome: str):
        self.__nome = nome

    def set_email(self, email: str):
        self.__email = email

    def set_telefone(self, telefone: str):
        self.__telefone = telefone

    def set_nascimento(self, nascimento: str):
        self.__nascimento = datetime.strptime(nascimento, "%d-%m-%Y").date()

    def to_string(self) -> str:
        # Retorna uma string formatada com todas as informações do contato
        nasc_fmt = self.__nascimento.strftime("%d/%m/%Y")  # Formatação da data
        return (
            f"ID         : {self.__id}\n"
            f"Nome       : {self.__nome}\n"
            f"Email      : {self.__email}\n"
            f"Telefone   : {self.__telefone}\n"
            f"Nascimento : {nasc_fmt}"
        )

    def __str__(self):
        return self.to_string()


class ContatoUI:
    def __init__(self):
        self.contatos = []  # Lista de contatos
        self.proximo_id = 1  # ID sequencial para os contatos

    def menu(self):
        while True:
            # Menu com as opções de operações
            print("""
========= Menu =========
1 - Inserir contato
2 - Listar contatos
3 - Atualizar contato
4 - Excluir contato
5 - Pesquisar por nome
6 - Aniversariantes por mês
0 - Sair
========================
""")
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                self.inserir()  # Inserir novo contato
            elif opcao == "2":
                self.listar()  # Listar todos os contatos
            elif opcao == "3":
                self.atualizar()  # Atualizar um contato
            elif opcao == "4":
                self.excluir()  # Excluir um contato
            elif opcao == "5":
                self.pesquisar()  # Pesquisar por nome
            elif opcao == "6":
                self.aniversariantes()  # Aniversariantes do mês
            elif opcao == "0":
                print("Saindo... Até logo!")  # Finalizar aplicação
                break
            else:
                print("Opção inválida. Tente novamente.")

    def inserir(self):
        print("\n=== Novo Contato ===")
        nome = input("Nome: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
        nascimento = input("Nascimento (DD-MM-YYYY): ")
        # Criação e inserção do novo contato
        contato = Contato(self.proximo_id, nome, email, telefone, nascimento)
        self.contatos.append(contato)
        self.proximo_id += 1  # Incrementa o ID para o próximo contato
        print("Contato inserido com sucesso!\n")

    def listar(self):
        print("\n=== Lista de Contatos ===")
        if not self.contatos:
            print("Nenhum contato cadastrado.")
        for contato in self.contatos:
            print(contato)
            print("-----------------------")

    def atualizar(self):
        try:
            id = int(input("ID do contato a atualizar: "))
            for contato in self.contatos:
                if contato.get_id() == id:
                    print("Deixe em branco para manter o valor atual.")
                    nome = input(f"Nome [{contato.get_nome()}]: ") or contato.get_nome()
                    email = input(f"Email [{contato.get_email()}]: ") or contato.get_email()
                    telefone = input(f"Telefone [{contato.get_telefone()}]: ") or contato.get_telefone()
                    nasc_atual = contato.get_nascimento().strftime("%d-%m-%Y")
                    nascimento = input(f"Nascimento [{nasc_atual}]: ") or nasc_atual
                    # Atualiza os dados
                    contato.set_nome(nome)
                    contato.set_email(email)
                    contato.set_telefone(telefone)
                    contato.set_nascimento(nascimento)
                    print("Contato atualizado.\n")
                    return
            print("Contato não encontrado.\n")
        except ValueError:
            print("ID inválido.\n")

    def excluir(self):
        try:
            id = int(input("ID do contato a excluir: "))
            for contato in self.contatos:
                if contato.get_id() == id:
                    self.contatos.remove(contato)
                    print("Contato excluído com sucesso.\n")
                    return
            print("Contato não encontrado.\n")
        except ValueError:
            print("ID inválido.\n")

    def pesquisar(self):
        termo = input("Digite as iniciais do nome: ").lower()
        encontrados = [c for c in self.contatos if c.get_nome().lower().startswith(termo)]
        print(f"\n=== resultados para '{termo}' ===")
        if not encontrados:
            print("Nenhum contato encontrado.")
        for contato in encontrados:
            print(contato)
            print("-----------------------")

    def aniversariantes(self):
        try:
            mes = int(input("Informe o número do mês (1-12): "))
            print(f"\n=== Aniversariantes do mês {mes} ===")
            encontrados = [c for c in self.contatos if c.get_nascimento().month == mes]
            if not encontrados:
                print("Nenum aniversariante encontrado.")
            for contato in encontrados:
                print(contato)
                print("-----------------------")
        except ValueError:
            print("Mês inválido.\n")


if __name__ == "__main__":
    ui = ContatoUI()
    ui.menu()
