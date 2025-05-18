from app.models.animal import Animal

class Gato(Animal):
     def __init__(self, nombre: str, color: str, edad: int, peso: float) -> None:
          super().__init__(nombre, edad, peso)
          self.__color = color

     def hacer_sonido(self) -> str:
          return "¡Miau, miau!"
     
     def get_color(self) -> str:
          return self.__color
     
     def set_color(self, color) -> None:
          self.__color = color

     def get_json(self) -> dict:
          return {
               "animal": "Gato",
               "sonido": self.hacer_sonido()
          }