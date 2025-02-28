from animal import Animal

class Animal_Granja(Animal):
     def __init__(self, nombre: str, peso: float, edad: int) -> None:
          super().__init__(nombre, edad, peso) 
          self._kilos_comidos = 0 

     def comer(self, kilos) -> None:
          self._kilos_comidos += kilos * 0.8

     def obtener_kilos_comidos(self) -> float:
          return self._kilos_comidos
