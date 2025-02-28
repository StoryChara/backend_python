from guarderia import Guarderia

from animal import Animal
from animal_exotico import Animal_Exotico
from animal_granja import Animal_Granja
from gato import Gato
from perro import Perro
from boa import Boa_Constrictor
from huron import Huron

# LOS TESTEOS FUERON CREADOS POR IA PARA AGILIZAR EL PROCESO

# Probando clase Animal
animal = Animal("Genérico", 5, 20.0)
print(f"Animal: {animal.get_nombre()}, Edad: {animal.get_edad()}, Peso: {animal.get_peso()}")

# Probando clase Gato
gato = Gato("Michi", "Negro", 3, 4.5)
print(f"Gato: {gato.get_nombre()}, Color: {gato.get_color()}, Sonido: {gato.hacer_sonido()}")

# Probando clase Perro
perro = Perro("Firulais", "Labrador", 4, 25.0)
print(f"Perro: {perro.get_nombre()}, Raza: {perro.get_raza()}, Sonido: {perro.hacer_sonido()}")

# Probando clase Animal Exótico
animal_exotico = Animal_Exotico("Tigre", 100.0, 7, "India", 500.0)
print(f"Animal Exótico: {animal_exotico.get_nombre()}, País de origen: {animal_exotico.get_pais_origen()}, Flete: {animal_exotico.calcular_flete()}")

# Probando clase Boa Constrictor
boa = Boa_Constrictor("Boa", 15.0, 5, "Brasil", 300.0)
boa.sumar_raton_comido()
print(f"Boa: {boa.get_nombre()}, Ratones comidos: {boa.get_ratones_comidos()}, Sonido: {boa.hacer_sonido()}")

# Probando clase Hurón
huron = Huron("Huroncito", 2.0, 2, "Argentina", 200.0)
print(f"Hurón: {huron.get_nombre()}, Sonido: {huron.hacer_sonido()}")

# Probando clase Animal Granja
vaca = Animal_Granja("Vaca", 300.0, 5)
vaca.comer(10)
print(f"Animal de Granja: {vaca.get_nombre()}, Kilos comidos: {vaca.obtener_kilos_comidos()}")

mi_guarderia = Guarderia("Guardería UwU", "Calle 123")

# Agregar animales a la guardería
mi_guarderia.add_animal(perro)
mi_guarderia.add_animal(gato)
mi_guarderia.add_animal(boa)
mi_guarderia.add_animal(huron)
mi_guarderia.add_animal(vaca)

# Mostrar los animales en la guardería
print(mi_guarderia.get_animales())