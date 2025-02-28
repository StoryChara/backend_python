class Guarderia:
    def __init__(self, nombre: str, ubicacion: str):
        self.__nombre = nombre
        self.__ubicacion = ubicacion
        self.__animales = []

    def get_nombre(self) -> str:
        return self.__nombre

    def get_ubicacion(self) -> str:
        return self.__ubicacion

    def get_animales(self) -> list:
        return self.__animales

    def set_nombre(self, nombre: str) -> None:
        self.__nombre = nombre

    def set_ubicacion(self, ubicacion: str) -> None:
        self.__ubicacion = ubicacion

    def add_animal(self, animal) -> None:
        self.__animales.append(animal)