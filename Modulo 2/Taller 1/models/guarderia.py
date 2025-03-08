from models.perro import Perro 

class Guarderia:
    def __init__(self, nombre: str, ubicacion: str, animales: list):
        self.__nombre = nombre
        self.__ubicacion = ubicacion
        self.__perros = animales  # Sé que me pide solo 3 perros como variables diferentes pero considero que una lista es mucho más útil

    def set_nombre(self, nombre: str) -> None:
        self.__nombre = nombre

    def set_ubicacion(self, ubicacion: str) -> None:
        self.__ubicacion = ubicacion

    def set_new_perro(self, perro: Perro) -> None:
        self.__perros.append(perro)

    def get_nombre(self) -> str:
        return self.__nombre

    def get_ubicacion(self) -> str:
        return self.__ubicacion
    
    def get_perros(self) -> list:
        return self.__perros

    def retornar_perros(self) -> tuple:
        return tuple(self.__perros)
