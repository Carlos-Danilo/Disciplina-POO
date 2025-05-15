#class Triangulo:
    #def __init__(self):
        #self.__b = 0
        #self.__h = 0
    #def calc_area(self):
        #return self.b * self.h / 2 
    
class Triangulo:
    def __init__(self):
        self.__b = 0  
        self.__h = 0  
    
    
    def get_base(self):
        return self.__b
    
    
    def set_base(self, valor):
        if valor <= 0:
            raise ValueError("A base deve ser um valor positivo.")
        self.__b = valor
    
    
    def get_altura(self):
        return self.__h
    
    
    def set_altura(self, valor):
        if valor <= 0:
            raise ValueError("A altura deve ser um valor positivo.")
        self.__h = valor
    
    
    def calc_area(self):
        return self.__b * self.__h / 2


def main():
    t = Triangulo()
    
    
    t.set_base(float(input("Digite o valor da base do triângulo: ")))
    
    
    t.set_altura(float(input("digite o valor da altura do triângulo: ")))
    
    
    print(f"A área do triângulo é {t.calc_area()}")


main()
