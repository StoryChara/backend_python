import unittest
from models.guarderia import Guarderia
from models.boa import Boa_Constrictor as Boa
from models.huron import Huron


class TestGuarderia(unittest.TestCase):
     guarderia = Guarderia(nombre="Guardería UwU", ubicacion="Calle 123")

     huron1 = Huron(nombre="Furret", peso=32.5, edad=2, pais_origen="Kanto", impuestos=0.25)
     huron2 = Huron(nombre="Sentret", peso=6, edad=2, pais_origen="Kanto", impuestos=0.25)
     boa1 = Boa(nombre="Ekans", peso=6.9, edad=2, pais_origen="Kanto", impuestos=0.25)
     boa2 = Boa(nombre="Arbok", peso=65, edad=2, pais_origen="Kanto", impuestos=0.25)

     guarderia.add_animal(huron1); guarderia.add_animal(huron2)
     guarderia.add_animal(boa1); guarderia.add_animal(boa2)

     