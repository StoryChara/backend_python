from ingrediente import Ingrediente

class Base(Ingrediente):
     def __init__(self, nombre: str, precio: float, calorias: int, inventario: int, es_vegetariano: bool, sabor: str):
          """Inicializa una base con los atributos heredados de ingrediente y su sabor."""
          super().__init__(nombre, precio, calorias, inventario, es_vegetariano)
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