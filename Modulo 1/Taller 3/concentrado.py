class Concentrado:
    def __init__(self, nombre: str, precio: float, calorias: int, registro_invima: str):
        self.__nombre = nombre
        self.__precio = precio
        self.__calorias = calorias
        self.__registro_invima = registro_invima

    def get_nombre(self) -> str:
        return self.__nombre

    def get_precio(self) -> float:
        return self.__precio

    def get_calorias(self) -> int:
        return self.__calorias

    def dar_informacion(self) -> str:
        return f"{self.__nombre} (${self.__precio})"

    def calcular_rentabilidad(self) -> float:
        return round(self.__precio / self.__calorias, 2)
