from animal import Animal

class Animal_Exotico(Animal):
     def __init__(self, nombre:str, peso:float, edad:int, pais_origen: str, impuestos:float) -> None:
          super().__init__(nombre, edad, peso)
          self._pais_origen = pais_origen
          self._impuestos = impuestos

     def get_pais_origen(self) -> float:
          return self._pais_origen
     
     def get_impuestos(self) -> float:
          return self._impuestos
     
     def set_pais_origen(self, pais:str) -> None:
          self._pais_origen = pais

     def set_impuestos(self, impuestos:float) -> None:
          self._impuestos = impuestos

     def calcular_flete(self) -> float:
          return self._impuestos * self.get_peso() 