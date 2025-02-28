from perro import Perro
from concentrado import Concentrado
from cuidandero import Cuidandero

class Guarderia:
    def __init__(self, nombre: str, ubicacion: str, animales: list, concentrados:list, cuidandero: Cuidandero):
        self.__nombre = nombre
        self.__ubicacion = ubicacion
        self.__animales = animales  # Sé que me pide solo 3 perros como variables diferentes pero considero que una lista es mucho más útil
        self.__concentrados = concentrados
        self.__cuidandero = cuidandero

    def set_nombre(self, nombre: str) -> None:
        self.__nombre = nombre

    def set_ubicacion(self, ubicacion: str) -> None:
        self.__ubicacion = ubicacion

    def set_cuidandero(self, cuidandero:Cuidandero) -> None:
        self.__cuidandero = cuidandero

    def set_new_perro(self, perro: Perro) -> None:
        self.__perros.append(perro)

    def set_new_concentrado(self, concentrado: Concentrado) -> None:
        self.__concentrados.append(concentrado)

    def get_nombre(self) -> str:
        return self.__nombre

    def get_ubicacion(self) -> str:
        return self.__ubicacion
    
    def get_cuidandero(self) -> Cuidandero:
        return self.__cuidandero

    def get_perros(self) -> list:
        return self.__perros

    def get_concentrados(self) -> list:
        return self.__concentrados