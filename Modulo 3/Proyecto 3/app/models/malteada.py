from app.models.iproducto import IProducto
from app.models.ingrediente import Ingrediente
import app.models.funciones as fn

class Malteada(IProducto):
     def __init__(self, id:int, nombre: str, precio_publico: float, volumen: int, ingrediente1: Ingrediente, ingrediente2: Ingrediente, ingrediente3: Ingrediente):
          """Inicializa una Malteada con su nombre, precio público, volumen y sus tres ingredientes."""
          self._id = id
          self._nombre = nombre
          self._precio_publico = precio_publico
          self._volumen = volumen
          self._ingrediente1 = ingrediente1
          self._ingrediente2 = ingrediente2
          self._ingrediente3 = ingrediente3

     def calcular_costo(self) -> float:
          """Calcula el costo total de producción de la malteada sumando los precios de los ingredientes más 500 pesos."""
          return fn.calcular_costo(self._ingrediente1.get_dict(), self._ingrediente2.get_dict(), self._ingrediente3.get_dict()) + 500

     def calcular_calorias(self) -> float:
          """Calcula el total de calorías de la malteada sumando las calorías de los ingredientes más 200."""
          calorias_lista = [self._ingrediente1.get_calorias(), self._ingrediente2.get_calorias(), self._ingrediente3.get_calorias()]
          return fn.contar_calorias(calorias_lista) + 200

     def calcular_rentabilidad(self) -> float:
          """Calcula la rentabilidad de la malteada restando el costo del precio público."""
          return fn.calcular_rentabilidad(self._precio_publico, self._ingrediente1.get_dict(), self._ingrediente2.get_dict(), self._ingrediente3.get_dict())

     # Getters 
     def get_nombre(self) -> str:
          return self._nombre

     def get_precio_publico(self) -> float:
          return self._precio_publico

     def get_volumen(self) -> int:
          return self._volumen

     def get_ingredientes(self) -> tuple:
          return self._ingrediente1, self._ingrediente2, self._ingrediente3
     
     def get_id(self) -> int:
          return self._id
     
     def get_dict(self) -> dict:
          return {
               "nombre": self._nombre,
               "rentabilidad": self.calcular_rentabilidad()
          }
     
     def to_dict_API_PUBLIC(self) -> dict:
          return {
               "id": self._id,
               "nombre": self._nombre,
               "precio_publico": self._precio_publico,
               "volumen": self._volumen,
               "ingredientes": {
                    "ingrediente 1": self._ingrediente1.to_dict_API_PUBLIC(),
                    "ingrediente 2": self._ingrediente2.to_dict_API_PUBLIC(),
                    "ingrediente 3": self._ingrediente3.to_dict_API_PUBLIC(),
               }
          }
     
     def to_dict_API_CLIENTE(self) -> dict:
          return {
               "id": self._id,
               "nombre": self._nombre,
               "precio_publico": self._precio_publico,
               "volumen": self._volumen,
               "ingredientes": {
                    "ingrediente 1": self._ingrediente1.to_dict_API_CLIENTE(),
                    "ingrediente 2": self._ingrediente2.to_dict_API_CLIENTE(),
                    "ingrediente 3": self._ingrediente3.to_dict_API_CLIENTE(),
               },
               "calorias": self.calcular_calorias()
          }
     
     def to_dict_API_FINANCE(self) -> dict:
          return {
               "id": self._id,
               "nombre": self._nombre,
               "precio_publico": self._precio_publico,
               "rentabilidad": self.calcular_rentabilidad(),
               "costo": self.calcular_costo()
          }

     # Setters

     def set_nombre(self, nombre: str):
          self._nombre = nombre

     def set_precio_publico(self, precio_publico: float):
          self._precio_publico = precio_publico

     def set_volumen(self, volumen: int):
          self._volumen = volumen

     def set_ingrediente1(self, ingrediente:Ingrediente):
          self._ingrediente1 = ingrediente

     def set_ingrediente2(self, ingrediente:Ingrediente):
          self._ingrediente2 = ingrediente

     def set_ingrediente3(self, ingrediente:Ingrediente):
          self._ingrediente3 = ingrediente