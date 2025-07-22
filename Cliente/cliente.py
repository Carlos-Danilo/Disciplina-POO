import json

class Cliente:
    def __init__(self,id, nome, email, fone):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__fone = fone
    def get_id(self):
        return self.__id    
    def get_nome(self):
        return self.__nome  
    def get_email(self):
        return self.__email  
    
    def set_id(self, id):
        self.__id = id
    
    def set_nome(self, nome):
        self.__nome = nome
    
    def set_email(self, email):
        self.__email = email
    
    def set_fone(self, fone):
        self.__fone = fone

    def cliente 

    def __str__(self):
        return f"ID: {self.__id} | nome: {self.__nome} | email: {self.__email} | Telefone: {self.__fone}"
    
    def to_dict(self): 
        return {'id': self.__id,'nome': self.__nome,'email': self.__email,'email': self.__email,}
      
    