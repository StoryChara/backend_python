import unittest
from models.heladeria import Heladeria
from models.base import Base
from models.complemento import Complemento
from models.copa import Copa
from models.malteada import Malteada

class TestHeladeria(unittest.TestCase):
     def setUp(self):
          self.base = Base("Helado", 2.0, 150, 10, True, "Dulce")
          self.comp1 = Complemento("Oreo", 1.0, 100, 5, True)
          self.comp2 = Complemento("Cereza", 0.5, 20, 8, True)
          self.producto = Copa("Copa Feliz", 6.0, "Cristal", self.base, self.comp1, self.comp2)
          self.heladeria = Heladeria(self.producto, self.producto, self.producto, self.producto, [self.base, self.comp1, self.comp2])

     def test_encontrar_mas_rentable(self):
          mas_rentable = self.heladeria.producto_mas_rentable()
          self.assertEqual(mas_rentable, "Copa Feliz")

     def test_vender_producto_exitoso(self):
          mensaje = self.heladeria.vender_producto("Copa Feliz")
          self.assertEqual(mensaje, "¡Vendido!")

     def test_vender_producto_no_existente(self):
          with self.assertRaises(ValueError):
               self.heladeria.vender_producto("Producto Fantasma")

     def test_vender_producto_sin_stock(self):
          self.base._inventario = 0.1
          with self.assertRaises(ValueError):
               self.heladeria.vender_producto("Copa Feliz")
