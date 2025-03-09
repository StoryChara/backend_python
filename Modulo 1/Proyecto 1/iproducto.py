from abc import ABC, abstractmethod

class IProducto(ABC):
     @abstractmethod
     def calcular_costo(self) -> float:
          """Calcula el costo total del producto."""
          pass

     @abstractmethod
     def calcular_rentabilidad(self) -> float:
          """Calcula la rentabilidad del producto."""
          pass

     @abstractmethod
     def calcular_calorias(self) -> float:
          """Calcula la cantidad de calorías del producto."""
          pass