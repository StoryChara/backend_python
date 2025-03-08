from models.guarderia import Guarderia 
from models.perro import Perro 

class Controller:
    def __init__(self):
        self.guarderia = Guarderia("Guardería UwU", "Calle 123", 
          [Perro("Rufo", "Labrador", 7, 22), 
            Perro("Bingo", "Pug", 2, 6),
            Perro("Lassie", "Collie", 5, 27)
          ])

    def retornar_perros(self):
        return self.guarderia.retornar_perros()