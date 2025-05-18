from app.models.animal_exotico import Animal_Exotico

class Huron(Animal_Exotico):
     def __init__(self, nombre:str, peso:float, edad:int, pais_origen: str, impuestos:float) -> None:
          super().__init__(nombre, peso, edad, pais_origen, impuestos)

     def hacer_sonido(self):
          return "¡Eek Eek!"
     
     def get_json(self) -> dict:
          return {
               "animal": "Hurón",
               "sonido": self.hacer_sonido()
          }