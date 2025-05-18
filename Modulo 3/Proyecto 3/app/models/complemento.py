from app.models.ingrediente import Ingrediente

class Complemento(Ingrediente):
     def __init__(self, id:int, nombre: str, precio: float, calorias: int, inventario: float, es_vegetariano: bool):
          """Inicializa un complemento con los atributos heredados de ingrediente."""
          super().__init__(id, nombre, precio, calorias, inventario, es_vegetariano)

     # Funciones
     def abastecer(self):
          """Abastece el inventario sumando 10 unidades."""
          self._inventario += 10

     def gastar(self):
          """Gasta 1 unidad del complemento al vender un producto."""
          if self._inventario >= 1:
               self._inventario -= 1

     def renovar_inventario(self, cantidad: float):
          """Restaura el inventario a 'cantidad' unidades."""
          self._inventario += cantidad

     def acabar_inventario(self):
          """Baja el inventario a 0 debido a baja rotación."""
          self._inventario = 0

     def to_dict_API_PUBLIC(self):
          return {
               "id": self._id,
               "nombre": self._nombre,
               "es_vegetariano": self._es_vegetariano,
          }
     
     def to_dict_API_CLIENTE(self):
          return {
               "id": self._id,
               "nombre": self._nombre,
               "calorias": self._calorias,
               "es_vegetariano": self._es_vegetariano,
               "calorias": self._calorias,
               "es_sano": self.es_sano(),
          }