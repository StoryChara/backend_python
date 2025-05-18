import unittest
from models.huron import Huron

class TestBoa(unittest.TestCase):
     huron = Huron(nombre="Furret", peso=32.5, edad=2, pais_origen="Kanto", impuestos=0.25)

     def test_hacer_sonido(self):
          self.assertEqual(self.huron.hacer_sonido(), "¡Eek Eek!")

     def test_calcular_flete(self):
          self.assertAlmostEqual(self.huron.calcular_flete(), 8.125)