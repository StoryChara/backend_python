from guarderia import Guarderia
from perro import Perro
from concentrado import Concentrado
from cuidandero import Cuidandero

concentrado1 = Concentrado("Dog Chow", 20000, 500, "INVIMA0123")
concentrado2 = Concentrado("Pedigree", 25000, 600, "INVIMA4567")
concentrado3 = Concentrado("Chunky"  , 15000, 650, "INVIMA8910")

concentrados = [concentrado1, concentrado2, concentrado3]

perro1 = Perro('Zeus', 'Rottweiler', 3, 45.8, concentrado1)
perro2 = Perro('Nala', 'Goldren R.', 1,  8.5, concentrado3)
perro3 = Perro('Atila', 'Alabai',    5, 58.9, concentrado2)
perro4 = Perro('Paca', 'French P.', 13, 30.0, concentrado1)

perros = [perro1, perro2, perro3, perro4]

cuidador = Cuidandero("Cesar Milan", "123456789")

g = Guarderia("Guardería UwU", "Calle 123", perros, concentrados, cuidador)