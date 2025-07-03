class Pais:
    def __init__(self, id, nome, populacao, area):
        self.id = id
        self.nome = nome
        self.populacao = populacao
        self.area = area

    def densidade(self):
        return self.populacao / self.area if self.area != 0 else 0

    def __str__(self):
        return f"{self.nome} (ID: {self.id}) - População: {self.populacao}, Área: {self.area} km², Densidade: {self.densidade():.2f} hab/km²"
        
class PaisUI:
    paises = []

    @staticmethod
    def main():
        while True:
            opcao = PaisUI.menu()
            if opcao == 1:
                PaisUI.inserir()
            elif opcao == 2:
                PaisUI.listar()
            elif opcao == 3:
                PaisUI.atualizar()
            elif opcao == 4:
                PaisUI.excluir()
            elif opcao == 5:
                PaisUI.mais_populoso()
            elif opcao == 6:
                PaisUI.mais_povoado()
            elif opcao == 7:
                print("Saindo...")
                break
            else:
                print("Opção inválida!")

    @staticmethod
    def menu():
        print("\nOpções:")
        print("1. Inserir novo país")
        print("2. Listar todos os países")
        print("3. Atualizar país")
        print("4. Excluir país")
        print("5. Mostrar país mais populoso")
        print("6. Mostrar país mais povoado")
        print("7. Sair")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1

    @staticmethod
    def inserir():
        try:
            id = int(input("ID: "))
            nome = input("Nome: ")
            populacao = int(input("População: "))
            area = float(input("Área: "))
            novo_pais = Pais(id, nome, populacao, area)
            PaisUI.paises.append(novo_pais)
            print("País inserido com sucesso!")
        except ValueError:
            print("Erro na entrada de dados. Tente novamente.")

    @staticmethod
    def listar():
        if not PaisUI.paises:
            print("Nenhum país cadastrado.")
        else:
            for pais in PaisUI.paises:
                print(pais)

    @staticmethod
    def atualizar():
        try:
            id = int(input("Digite o ID do país que deseja atualizar: "))
            for pais in PaisUI.paises:
                if pais.id == id:
                    pais.nome = input("Novo nome: ")
                    pais.populacao = int(input("Nova população: "))
                    pais.area = float(input("Nova área: "))
                    print("País atualizado com sucesso!")
                    return
            print("País não encontrado.")
        except ValueError:
            print("Entrada inválida.")

    @staticmethod
    def excluir():
        try:
            id = int(input("Digite o ID do país que deseja excluir: "))
            for pais in PaisUI.paises:
                if pais.id == id:
                    PaisUI.paises.remove(pais)
                    print("País excluído com sucesso!")
                    return
            print("País não encontrado.")
        except ValueError:
            print("ID inválido.")

    @staticmethod
    def mais_populoso():
        if not PaisUI.paises:
            print("Nenhum país cadastrado.")
            return
        mais = max(PaisUI.paises, key=lambda p: p.populacao)
        print("País mais populoso:")
        print(mais)

    @staticmethod
    def mais_povoado():
        if not PaisUI.paises:
            print("Nenhum país cadastrado.")
            return
        mais = max(PaisUI.paises, key=lambda p: p.densidade())
        print("País mais povoado:")
        print (mais)
       
PaisUI.main()

