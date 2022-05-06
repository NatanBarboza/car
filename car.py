class Car:
    def __init__(self, model:str, consumption:float):
        self.__model = model
        self.__consumption = consumption
        self.__gas_tank = 0

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_model):
        self.__model = new_model

    @property
    def consumption(self):
        return self.__consumption

    @property
    def gas_tank(self):
        return self.__gas_tank

    def get_gas(self, value):
        self.__gas_tank += value
    
    def travel(self, distance):
        if(self.__gas_tank > 0):
            self.__gas_tank -= distance / self.__consumption