class Cuidandero:
     def __init__(self, nombre: str, identificacion: int):
          self.__nombre = nombre
          self.__identificacion = identificacion
     
     def get_nombre(self) -> str:
          return self.__nombre
    
     def get_identificacion(self) -> int:
        return self.__identificacion

     def set_nombre(self, nombre: str) -> None:
        self.__nombre = nombre

     def set_identificacion(self, identificacion: int) -> None:
        self.__identificacion = identificacion
