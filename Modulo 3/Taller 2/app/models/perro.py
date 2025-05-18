from app.models.animal import Animal

class Perro(Animal):
     def __init__(self, nombre: str, raza: str, edad: int, peso: float):
          super().__init__(nombre, edad, peso)
          self.__raza = raza

     def hacer_sonido(self):
          return "¡Guau, guau!"
     
     def get_raza(self):
          return self.__raza
     
     def set_raza(self, raza):
          self.__raza = raza

     def get_json(self) -> dict:
          return {
               "animal": "Perro",
               "sonido": self.hacer_sonido()
          }