class Viagem:
    def __init__(self, destino, distancia_km, litros_combustivel):
        self.__destino = destino
        self.__distancia_km = distancia_km
        self.__litros_combustivel = litros_combustivel

    def get_destino(self):
        return self.__destino

    def get_distancia_km(self):
        return self.__distancia_km

    def get_litros_combustivel(self):
        return self.__litros_combustivel

   
    def set_destino(self, destino):
        self.__destino = destino

    def set_distancia_km(self, distancia_km):
        self.__distancia_km = distancia_km

    def set_litros_combustivel(self, litros_combustivel):
        self.__litros_combustivel = litros_combustivel

    
    def consumo(self):
        if self.__litros_combustivel > 0:
            return self.__distancia_km / self.__litros_combustivel
        else:
            return 0

class ViagemUI:
    def __init__(self):
        pass

    def menu(self):
        print("\n1 - Calcular consumo médio")
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
        destino = input("\nDigite o destino da viagem: ")
        distancia_km = float(input("Digite a distância percorrida em km: "))
        litros_combustivel = float(input("Digite a quantidade de combustível gasta em litros: "))

        viagem = Viagem(destino, distancia_km, litros_combustivel)

        
        print("\nDados da viagem:")
        print(f"Destino: {viagem.get_destino()}")
        print(f"Distância: {viagem.get_distancia_km()} km")
        print(f"Combustível gasto: {viagem.get_litros_combustivel()} litros")

        
        consumo_medio = viagem.consumo()
        print(f"\nConsumo médio: {consumo_medio:.2f} km/litro")

if __name__ == "__main__":
    viagem_ui = ViagemUI()
    viagem_ui.main()