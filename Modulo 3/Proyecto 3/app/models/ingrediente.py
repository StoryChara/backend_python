from abc import ABC, abstractmethod
import app.models.funciones as fn

class Ingrediente(ABC):
    def __init__(self, id:int, nombre: str, precio: float, calorias: int, inventario: float, es_vegetariano: bool):
        """Inicializa un ingrediente con nombre, precio, calorías, inventario y si es vegetariano."""
        self._id = id
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

    def get_calorias(self) -> int:
        return self._calorias

    def get_inventario(self) -> int:
        return self._inventario

    def get_es_vegetariano(self) -> bool:
        return self._es_vegetariano
    
    def get_id(self) -> int:
        return self._id

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

    def set_calorias(self, nuevas_calorias: int):
        if nuevas_calorias >= 0:
            self._calorias = nuevas_calorias

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