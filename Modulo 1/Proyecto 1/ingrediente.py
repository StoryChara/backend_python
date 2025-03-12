from abc import ABC, abstractmethod
import funciones as fn

class Ingrediente(ABC):
    def __init__(self, nombre: str, precio: float, calorias: int, inventario: float, es_vegetariano: bool):
        """Inicializa un ingrediente con nombre, precio, calorías, inventario y si es vegetariano."""
        self._nombre = nombre
        self._precio = precio
        self._calorias = calorias
        self._inventario = inventario
        self._es_vegetariano = es_vegetariano

    # Getters
    def get_nombre(self) -> str:
        return self._nombre

    def get_precio(self) -> float:
        return self._precio

    def get_calorías(self) -> int:
        return self._calorías

    def get_inventario(self) -> int:
        return self._inventario

    def get_es_vegetariano(self) -> bool:
        return self._es_vegetariano

    def get_dict(self) -> dict:
        """Convierte el ingrediente en un diccionario para facilitar su uso en funciones."""
        return {
            "nombre": self._nombre,
            "precio": self._precio
        }

    # Setters
    def set_precio(self, nuevo_precio: float):
        if nuevo_precio >= 0:
            self._precio = nuevo_precio

    def set_calorías(self, nuevas_calorías: int):
        if nuevas_calorías >= 0:
            self._calorías = nuevas_calorías

    def set_inventario(self, nuevo_inventario: int):
        if nuevo_inventario >= 0:
            self._inventario = nuevo_inventario

    def set_es_vegetariano(self, vegetariano: bool):
        self._es_vegetariano = vegetariano

    # Funciones
    def es_sano(self) -> bool:
        """Determina si un ingrediente es sano (menos de 100 calorías o vegetariano)."""
        return fn.es_sano(self._calorias, self._es_vegetariano)

    @abstractmethod
    def abastecer(self, cantidad: int):
        """Método abstracto para abastecer el inventario del ingrediente."""
        pass

    @abstractmethod
    def gastar(self):
        """Método abstracto para descontar ingredientes del inventario al vender."""
        pass