from models.boa import Boa_Constrictor as Boa

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

    def alimentar_boa(self, boa_alimentar:Boa):
        try:
            if (boa_alimentar is None) or (boa_alimentar not in self.__animales):
                raise ValueError("Esta Boa no existe!")  
            
            boa_alimentar.alimentar()
            
        except ValueError as e:
            if str(e) == "Demasiados Ratones!":
                return "La boa está llena."
            
            return f"Error: {e}"
        
        else:
            return "Éxito"