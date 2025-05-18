import unittest
from models.base import Base
from models.complemento import Complemento
from models.copa import Copa
from models.malteada import Malteada

class TestProductos(unittest.TestCase):
     def setUp(self):
          self.base = Base("Vainilla", 2.0, 150, 10, True, "Dulce")
          self.comp1 = Complemento("Galleta", 1.0, 100, 5, True)
          self.comp2 = Complemento("Fresa", 0.5, 20, 8, True)
          self.copa = Copa("Copa Amor", 6.0, "Cristal", self.base, self.comp1, self.comp2)
          self.malteada = Malteada("Malteada Choco", 7.0, 500, self.base, self.comp1, self.comp2)

     def test_calorias(self):
          self.assertEqual(self.copa.calcular_calorias(), 256.5)
          self.assertEqual(self.malteada.calcular_calorias(), 470)

     def test_costo_produccion(self):
          self.assertAlmostEqual(self.copa.calcular_rentabilidad(), 2.5)

     def test_rentabilidad(self):
          self.assertAlmostEqual(self.copa.calcular_rentabilidad(), 2.5)