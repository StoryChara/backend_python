import unittest
from models.base import Base
from models.complemento import Complemento

class TestIngredientes(unittest.TestCase):
    def test_ingrediente_sano(self):
        base = Base("Yogurt", 2.5, 90, 10, True, "Frutal")
        complemento = Complemento("Granola", 1.0, 60, 20, True)
        self.assertTrue(base.es_sano())
        self.assertTrue(complemento.es_sano())

    def test_abastecer_ingrediente(self):
        base = Base("Yogurt", 2.5, 90, 10, True, "Frutal")
        comp = Complemento("Chocolate", 1.0, 100, 2, True)
        comp.abastecer()
        base.abastecer()
        self.assertEqual(comp.get_inventario(), 12)
        self.assertEqual(base.get_inventario(), 15)
