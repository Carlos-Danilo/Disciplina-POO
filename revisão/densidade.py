class  País:
    def __init__(self, nome, populacao, area):
        self.__nome = nome
        self.__populacao = populacao
        self.__area = area

    def get_nome(self):
        return self.__nome
    def get_populacao(self):
        return self.__populacao
    def get_area(self):
        return self.__area
    
    def set_nome(self, nome):
        self.__nome = nome
    def set_populacao(self, populacao):
        self.__populacao = populacao
    def set_area(self, area):
        self.__area = area

    def densidade(self):
        return self.__populacao / self.__area
    
class UIPaís:
    def __init__(self):
        pass

    def menu(self):
        print("\n1 - Calcular densidade populacional")
        print("2 - Sair")
        return int(input("Escolha uma opção: "))

    def main(self):
        while True:
            opcao = self.menu()
            if opcao == 1:
                self.calculo()
            elif opcao == 2:
                print("\nAté mais!")
                break
            else:
                print("\nOpção inválida. Tente novamente.")

    def calculo(self):
        nome = input("\nDigite o nome do país: ")
        populacao = int(input("Digite a população do país: "))
        area = float(input("Digite a área do país em km²: "))

        pais = País(nome, populacao, area)

        print(f"\nDensidade populacional de {pais.get_nome()}: {pais.densidade()} habitantes por km²")

if __name__ == "__main__":
    ui = UIPaís()
    ui.main()

