from abc import ABC, abstractmethod

class iAnimal(ABC):
     @abstractmethod
     def comer(self, kilos) -> None:
          pass

     @abstractmethod
     def obtener_kilos_comidos(self) -> None:
          pass