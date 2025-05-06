class circulo:
    def __init__(self):
        self.raio = 2

    def area(self):
        return 3.14 * (self.raio ** 2)

    def perimetro(self):
        return 2 * 3.14 * self.raio
    def __str__(self):
        return f'Raio: {self.raio}, Area: {self.area()}, Perimetro: {self.perimetro()}'
   
    def __eq__(self, other):
        return self.raio == other.raio

teste = circulo()
raio = float(input('Digite o raio do circulo: '))
teste.raio = raio
print(teste.raio)
raio2 = float(input('Digite o raio do circulo: '))
teste2 = circulo(raio2)
print(teste2)