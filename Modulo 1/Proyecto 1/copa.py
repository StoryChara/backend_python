from iproducto import IProducto
import funciones as fn
from ingrediente import Ingrediente

class Copa(IProducto):
     """Clase que representa una copa de helado."""

     def __init__(self, nombre: str, precio_publico: float, tipo_vaso: str, ingrediente1: Ingrediente, ingrediente2: Ingrediente, ingrediente3: Ingrediente):
          """Inicializa una Copa con su nombre, precio público, tipo de vaso y sus tres ingredientes."""
          self._nombre = nombre
          self._precio_publico = precio_publico
          self._tipo_vaso = tipo_vaso
          self._ingrediente1 = ingrediente1
          self._ingrediente2 = ingrediente2
          self._ingrediente3 = ingrediente3

     # Funciones
     def calcular_costo(self) -> float:
          """Calcula el costo total de producción de la copa sumando los precios de los tres ingredientes."""
          return fn.calcular_costo(self._ingrediente1.get_dict(), self._ingrediente2.get_dict(), self._ingrediente3.get_dict())

     def calcular_calorias(self) -> float:
          """Calcula el total de calorías de la copa usando la fórmula con 0.95."""
          calorias_lista = [self._ingrediente1.get_calorias(), self._ingrediente2.get_calorias(), self._ingrediente3.get_calorias()]
          return fn.contar_calorias(calorias_lista)*0.95

     def calcular_rentabilidad(self) -> float:
          """Calcula la rentabilidad de la copa restando el costo del precio público."""
          return fn.calcular_rentabilidad(self._precio_publico, self._ingrediente1.get_dict(), self._ingrediente2.get_dict(), self._ingrediente3.get_dict())

     # Getters
     def get_nombre(self) -> str:
          return self._nombre

     def get_precio_publico(self) -> float:
          return self._precio_publico

     def get_tipo_vaso(self) -> str:
          return self._tipo_vaso

     def get_ingredientes(self) -> tuple:
          return self._ingrediente1, self._ingrediente2, self._ingrediente3
     
     def get_dict(self) -> dict:
          return {
               "nombre": self._nombre,
               "rentabilidad": self.calcular_rentabilidad()
          }
     
     # Setters
     def set_nombre(self, nombre: str):
          self._nombre = nombre

     def set_precio_publico(self, precio_publico: float):
          self._precio_publico = precio_publico

     def set_tipo_vaso(self, tipo_vaso: str):
          self._tipo_vaso = tipo_vaso

     def set_ingrediente1(self, ingrediente:Ingrediente):
          self._ingrediente1 = ingrediente

     def set_ingrediente2(self, ingrediente:Ingrediente):
          self._ingrediente2 = ingrediente

     def set_ingrediente3(self, ingrediente:Ingrediente):
          self._ingrediente3 = ingrediente