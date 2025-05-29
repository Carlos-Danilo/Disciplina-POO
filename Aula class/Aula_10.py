
class retangulo:
    def __init__(self):
        self.__base = ""
        self.__altura = ""

    def set_base (self, base):
        if base < 1 : raise ValueError("O número deve ser positivo")
    def get_base (self):
        return self.__base
    
    def set_altura(self, altura):
        if altura < 1 : raise ValueError
    def get_altura(self):
        return self.__altura

    def set_area (self):
        return self.__base * self.__altura
    
    def set_diagonal (self):
        return self.__base**2 + self.__altura**2

    def __str__(self):
        return f"Base = {self.__base}- Altura {self.__altura}"

























































































