from copa import Copa
from malteada import Malteada
from ingrediente import Ingrediente
from base import Base
from complemento import Complemento
from iproducto import IProducto
import funciones as fn

class Heladeria:
     """Clase que representa una heladería."""

     def __init__(self, producto1: IProducto, producto2: IProducto, producto3: IProducto, producto4: IProducto, ingredientes: list[Ingrediente]):
          """Inicializa la heladería con su nombre, una lista de productos y un inventario de ingredientes."""
          self._producto1 = producto1
          self._producto2 = producto2
          self._producto3 = producto3
          self._producto4 = producto4
          self._inventario = ingredientes
          self._contador_ventas = 0 

     # Getters
     def get_productos(self) -> tuple:
          return self._producto1, self._producto2, self._producto3

     def get_inventario(self) -> list:
          return self._inventario

     def get_contador_ventas(self) -> int:
          return self._contador_ventas

     # Setters
     def set_producto1(self, producto:IProducto):
          self._producto1 = producto

     def set_producto2(self, producto:IProducto):
          self._producto2 = producto

     def set_producto3(self, producto:IProducto):
          self._producto3 = producto

     def set_producto4(self, producto:IProducto):
          self._producto4 = producto

     def add_ingrediente(self, ingrediente: Ingrediente):
          self._inventario.append(ingrediente)

     # Funciones
     def producto_mas_rentable(self) -> str:
          """Determina el producto más rentable de la heladería."""
          return fn.producto_mas_rentable(self._producto1.get_dict(), self._producto2.get_dict(), self._producto3.get_dict(), self._producto4.get_dict())

     def vender_producto(self, nombre_producto: str) -> bool:
          """Determina si es posible vender el producto."""
          productos = [self._producto1, self._producto2, self._producto3, self._producto4]
          producto_a_vender = next((p for p in productos if p.get_nombre() == nombre_producto), None)

          if producto_a_vender is None:
               return False
          
          ingredientes: tuple[Ingrediente, Ingrediente, Ingrediente] = producto_a_vender.get_ingredientes()

          for ingrediente in ingredientes:
               if isinstance(ingrediente, Base) and ingrediente.get_inventario() < 0.2:
                    return False
               elif isinstance(ingrediente, Complemento) and ingrediente.get_inventario() < 1:
                    return False
               
          for ingrediente in ingredientes:
               ingrediente.gastar()

          self._contador_ventas += producto_a_vender.get_precio_publico()
          return True