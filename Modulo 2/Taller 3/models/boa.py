from models.animal_exotico import Animal_Exotico

class Boa_Constrictor(Animal_Exotico):
     def __init__(self, nombre:str, peso:float, edad:int, pais_origen: str, impuestos:float) -> None:
          super().__init__(nombre, peso, edad, pais_origen, impuestos)
          self._ratones_comidos = 0

     def hacer_sonido(self) -> str:
          return "¡Tsss!"
     
     def get_ratones_comidos(self) -> int:
          return self._ratones_comidos
     
     def set_ratones_comidos(self, ratones) -> int:
          self._ratones_comidos = ratones

     def alimentar(self) -> str:
          if self._ratones_comidos >= 20:
               raise ValueError("Demasiados Ratones!")
          self._ratones_comidos += 1
          return "¡La boa fue alimentada!"
