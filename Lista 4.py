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