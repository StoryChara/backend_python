from app.models.iAnimal import iAnimal

class Animal(iAnimal):
     def __init__(self, nombre:str, edad:int, peso:float) -> None:
          self.__nombre = nombre
          self.__edad = edad
          self.__peso = peso

     def get_nombre(self) -> str:
          return self.__nombre

     def get_edad(self) -> int:
          return self.__edad

     def get_peso(self) -> float:
          return self.__peso

     def  set_nombre(self, nombre: str) -> None:
         self.__nombre = nombre

     def set_edad(self, edad: int) -> None:
          self.__edad = edad

     def set_peso(self, peso: float) -> None:
          self.__peso = peso

     def comer(self, kilos) -> None:
          self._kilos_comidos += kilos

     def obtener_kilos_comidos(self) -> float:
          return self._kilos_comidos
     
     def hacer_sonido(self) -> None:
          pass

