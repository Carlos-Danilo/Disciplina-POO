import random

class Bingo:
    def __init__(self, total):
        self.total = total
        self.sorteados = []

    def sortear(self):
        if len(self.sorteados) >= self.total:
            return -1 

        while True:
            num = random.randint(1, self.total)
            if num not in self.sorteados:
                self.sorteados.append(num)
                return num

    def get_sorteados(self):
        return self.sorteados

class BingoUI:
    def __init__(self):
        self.jogo = None

    def menu(self):
        while True:
            print("\n=== BINGO ===")
            print("1. Novo jogo")
            print("2. Sortear número")
            print("3. Ver sorteados")
            print("4. Sair")
            op = input("Escolha: ")

            if op == "1":
                self.novo_jogo()
            elif op == "2":
                self.sortear()
            elif op == "3":
                self.ver_sorteados()
            elif op == "4":
                print("Saindo do jogo...")
                break
            else:
                print("Opção inválida!")

    def novo_jogo(self):
        try:
            n = int(input("Total de bolas: "))
            if n > 0:
                self.jogo = Bingo(n)
                print("Novo jogo iniciado!")
            else:
                print("Número deve ser maior que zero.")
        except:
            print("Entrada inválida.")

    def sortear(self):
        if not self.jogo:
            print("Inicie um jogo primeiro.")
            return

        num = self.jogo.sortear()
        if num == -1:
            print("Todas as bolas já foram sorteadas.")
        else:
            print("Número sorteado:", num)

    def ver_sorteados(self):
        if not self.jogo:
            print("Inicie um jogo primeiro.")
            return

        lista = self.jogo.get_sorteados()
        if lista:
            print("Sorteados:", ", ".join(map(str, lista)))
        else:
            print("Nenhum número foi sorteado ainda.")


if __name__ == "__main__":
    ui = BingoUI()
    ui.menu()