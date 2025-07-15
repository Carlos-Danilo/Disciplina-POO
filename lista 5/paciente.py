from datetime import datetime

class Paciente:
    def __init__(self, nome: str, cpf: str, telefone: str, nascimento: str):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__nascimento = datetime.strptime(nascimento, "%d-%m-%Y").date()

    def get_nome(self):
        return self.__nome

    def get_cpf(self):
        return self.__cpf

    def get_telefone(self):
        return self.__telefone

    def get_nascimento(self):
        return self.__nascimento

    def set_nome(self, nome):
        self.__nome = nome

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def set_telefone(self, telefone):
        self.__telefone = telefone

    def set_nascimento(self, nascimento):
        self.__nascimento = datetime.strptime(nascimento, "%d-%m-%Y").date()

    def idade(self):
        hoje = datetime.today().date()
        anos = hoje.year - self.__nascimento.year
        meses = hoje.month - self.__nascimento.month
        if hoje.day < self.__nascimento.day:
            meses -= 1
        if meses < 0:
            anos -= 1
            meses += 12
        return f"{anos} anos e {meses} meses"

    def to_string(self):
        nasc_fmt = self.__nascimento.strftime("%d/%m/%Y")
        return (
            f"Nome      : {self.__nome}\n"
            f"CPF       : {self.__cpf}\n"
            f"Telefone  : {self.__telefone}\n"
            f"Nascimento: {nasc_fmt}\n"
            f"Idade     : {self.idade()}"
        )

    def __str__(self):
        return self.to_string()

def cadastrar_paciente():
    print("\n=== Cadastro de Paciente ===")
    nome = input("Noe completo: ")
    cpf = input("CPF (000.000.000-00): ")
    telefone = input("telefone")
    nascimento = input("Data de nascimento (dia-mês-ano): ")
    return Paciente(nome, cpf, telefone, nascimento)

def mostrar_paciente(paciente):
    print("\n Dados do Paciente")
    print(paciente)

def editar_paciente(paciente):
    print("\n Editar Paciente")


    nome_input = input(f"Nome [{paciente.get_nome()}]: ")
    if nome_input != "":
        paciente.set_nome(nome_input)

    cpf_input = input(f"CPF [{paciente.get_cpf()}]: ")
    if cpf_input != "":
        paciente.set_cpf(cpf_input)

    telefone_input = input(f"Telefone [{paciente.get_telefone()}]: ")
    if telefone_input != "":
        paciente.set_telefone(telefone_input)

    nascimento_input = input(
        f"Nascimento dia-mês-ano [{paciente.get_nascimento().strftime('%d-%m-%Y')}]: "
    )
    if nascimento_input != "":
        paciente.set_nascimento(nascimento_input)

    print("\nPaciente atualizado com sucesso!\n")

def menu():
    paciente = None
    while True:
        print("Menu")
        print("1 - Cadastrar paciente")
        print("2 - Mostrar paciente")
        print("3 - Editar paciente")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            paciente = cadastrar_paciente()
        elif opcao == "2":
            if paciente:
                mostrar_paciente(paciente)
            else:
                print("\nNenhum paciente cadastrado.\n")
        elif opcao == "3":
            if paciente:
                editar_paciente(paciente)
            else:
                print("\nNenhum paciente cadastrado.\n")
        elif opcao == "0":
            print("Saindo")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
