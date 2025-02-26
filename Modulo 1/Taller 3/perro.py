from concentrado import Concentrado

class Perro:
    def __init__(self, nombre: str, raza: str, edad: int, peso: float, concentrado: Concentrado):
        self.__nombre = nombre
        self.__raza = raza
        self.__edad = edad
        self.__peso = peso
        self.__concentrado_fav = concentrado

    def get_nombre(self) -> str:
        return self.__nombre
    
    def get_raza(self) -> str:
        return self.__raza
    
    def get_edad(self) -> int:
        return self.__edad
    
    def get_peso(self) -> float:
        return self.__peso
    
    def get_concentrado(self) -> Concentrado:
       return self.__concentrado_fav
    
    def set_nombre(self, nombre: str) -> None:
        self.__nombre = nombre

    def set_raza(self, raza: str) -> None:
        self.__raza = raza

    def set_edad(self, edad: int) -> None:
        self.__edad = edad

    def set_peso(self, peso: float) -> None:
        self.__peso = peso

    def set_concentrado(self, concentrado: Concentrado) -> None:
        self.__concentrado_fav = concentrado

    def ladrar(self) -> str:
        return "Guau Guau!!"

    def cambio_peso(self, nuevo_peso: float) -> None:
        self.__peso = nuevo_peso
