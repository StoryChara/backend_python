from app.models.ingrediente import Ingrediente
from app.config.db import db

class Base(Ingrediente):
     def __init__(self, id:int, nombre: str, precio: float, calorias: int, inventario: float, es_vegetariano: bool, sabor: str):
          """Inicializa una base con los atributos heredados de ingrediente y su sabor."""
          super().__init__(id, nombre, precio, calorias, inventario, es_vegetariano)
          self._sabor = sabor

     # Getters
     def get_sabor(self) -> str:
          return self._sabor
     
     # Setters
     def set_sabor(self, nuevo_sabor: str):
          self._sabor = nuevo_sabor

     # Funciones
     def abastecer(self):
          """Abastece el inventario sumando 5 unidades."""
          self._inventario += 5

     def gastar(self):
          """Gasta 0.2 unidades de la base al vender un producto."""
          if self._inventario >= 0.2:
               self._inventario -= 0.2

     def renovar_inventario(self, cantidad: float):
          """Restaura el inventario a 'cantidad' unidades."""
          self._inventario += cantidad

     def to_dict_API_PUBLIC(self):
          return {
               "id": self._id,
               "nombre": self._nombre,
               "es_vegetariano": self._es_vegetariano,
               "sabor": self._sabor
          }
     
     def to_dict_API_CLIENTE(self):
          return {
               "id": self._id,
               "nombre": self._nombre,
               "calorias": self._calorias,
               "es_vegetariano": self._es_vegetariano,
               "calorias": self._calorias,
               "es_sano": self.es_sano(),
               "sabor": self._sabor,
          }