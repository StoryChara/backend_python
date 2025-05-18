import unittest
from models.boa import Boa_Constrictor as Boa

class TestBoa(unittest.TestCase):
     boa = Boa(nombre="ekans", peso=6.9, edad=2, pais_origen="Kanto", impuestos=0.25)

     def test_hacer_sonido(self):
          self.assertEqual(self.boa.hacer_sonido(), "¡Tsss!")

     def test_calcular_flete(self):
          self.assertAlmostEqual(self.boa.calcular_flete(), 1.725)

     def test_alimentar(self):
          self.assertEqual(self.boa.alimentar(), "¡La boa fue alimentada!")