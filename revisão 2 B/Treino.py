from datetime import datetime

class treino:
    def __init__(self, id, data, distancia, tempo_da_corrida):
        self.set_id = (id)
        self.set_data =  (datetime.strptime(data, "%d-%m-%Y").date())
        self.set_distancia = (distancia)
        self.set_tempo_da_corrida =  (datetime.strptime(tempo_da_corrida, "%d-%m-%Y").date())
       
    def set_id(self, id):
        return self.__id 
    def set_data(self, data):
        return self.__data
    def set_distancia(self, distancia):
        return self.__distacia
    def set_tempo_da_corrida(self, tempo_da_corrida):
        return self.__tempo_da_corrida

    def get_id(self):
        return self.__id
    def get_data(self):
        return self.__data
    def get_distancia(self):
        return self.__distacia
    def get_tempo_da_corrida(self):
        return self.__tempo_da_corrida
