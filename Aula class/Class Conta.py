class Conta :
    def __init__(self):
        self.titular = ""
        self.numero = ""
        self.saldo = 0.0
    def set_titular(self,t):
        if t=="": raise ValueError()
        self.__titular=t
    def get_titular(self):
        return self.__titular    
    def set_numero(self):
        return self.__numero  
    def depositar(self, v):
        if v <= 0: raise ValueError()
        self.__saldo += v                                  
    def sacar(self, v):
        if v <= 0: raise ValueError()
        if v > self.__saldo: raise ValueError()
        self.__saldo -= v    
class UI :
    @staticmethod
    def main():
        x=Conta()
        x.set_titular(input())
        x.set_numero(input())
        x.depositar(float(input()))
        print(f"Você tem {x.get_self()}")
UI.main()        