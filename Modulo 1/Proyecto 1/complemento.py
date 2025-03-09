from ingrediente import Ingrediente

class Complemento(Ingrediente):
     def __init__(self, nombre: str, precio: float, calorias: int, inventario: int, es_vegetariano: bool):
          """Inicializa un complemento con los atributos heredados de ingrediente."""
          super().__init__(nombre, precio, calorias, inventario, es_vegetariano)

     # Funciones
     def abastecer(self):
          """Abastece el inventario sumando 10 unidades."""
          self._inventario += 10

     def gastar(self):
          """Gasta 1 unidad del complemento al vender un producto."""
          if self._inventario >= 1:
               self._inventario -= 1

     def renovar_inventario(self, cantidad: int):
          """Restaura el inventario a 'cantidad' unidades."""
          self._inventario += cantidad
