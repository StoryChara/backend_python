## María José Jara Herrera

## Punto 1
def calcular_IMC(peso:int, altura:float) -> float:
  """función para calcular el IM de una persona, dado su peso en (kg) y su altura en (mts)"""
  return "{:.2f}".format(round(peso / (altura ** 2), 2))

## Punto 2
def calcular_bisiesto(year: int) -> bool:
  """determina si un año es bisiesto según las reglas establecidas."""
  if year%4 == 0:
    if year%100 == 0 and year%400 == 0:
     return True
  return False


## Punto 3
def calcular_divisores(num1:int, num2:int) -> list:
  """función para calcular los divisores de dos números enteros positivos entre 1 y 100"""
  return [i for i in range(1, 101) if i%num1==0 and i%num2==0]

## Punto 4
def clasificar_palabras(palabras:list) -> dict:
  """función para clasificar las palabras de una lista de acuerdo a la cantidad de letras"""
  return {palabra: len(palabra) for palabra in palabras}

## LOS CASOS DE PRUEBA HAN SIDO GENERADOS POR IA PARA OBTENER LOS 
## RESULTADOS ESPERADOS CORRECTOS Y HACER LA DEBIDA COMPARACIÓN

print("\n - Punto 1:")
print(calcular_IMC(70, 1.75))  # 22.86 
print(calcular_IMC(50, 1.60))  # 19.53 
print(calcular_IMC(90, 1.75))  # 29.39 
print(calcular_IMC(45, 1.50))  # 20.00 
print(calcular_IMC(120, 1.80)) # 37.04 
print(calcular_IMC(42, 1.63))

print("\n - Punto 2:")
print(calcular_bisiesto(2024))  # True 
# Aunque 2024 sea bisiesto, según las reglas dadas, no será valido ya que debe ser divisible por 100 y 400 al mismo tiempo, algo que 2024 no cumple
print(calcular_bisiesto(1900))  # False
print(calcular_bisiesto(2000))  # True 
print(calcular_bisiesto(2023))  # False
print(calcular_bisiesto(2400))  # True 
print(calcular_bisiesto(2025))

print("\n - Punto 3:")
print(calcular_divisores(10, 3))  # [30, 60, 90]
print(calcular_divisores(5, 2))   # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(calcular_divisores(7, 3))   # [21, 42, 63, 84]
print(calcular_divisores(4, 6))   # [12, 24, 36, 48, 60, 72, 84, 96]
print(calcular_divisores(1, 50))  # [50, 100]

print("\n - Punto 4:")
print(clasificar_palabras(["Muchos", "años", "después", "frente", "al"])) # {'Muchos': 6, 'años': 4, 'después': 7, 'frente': 6, 'al': 2}
print(clasificar_palabras(["Python", "es", "genial"])) # {'Python': 6, 'es': 2, 'genial': 6}
print(clasificar_palabras(["computadora", "ratón", "teclado", "monitor"])) # {'computadora': 11, 'ratón': 5, 'teclado': 7, 'monitor': 7}
print(clasificar_palabras([]))  # {} (Lista vacía)
print(clasificar_palabras(['Hola', 'Mundo', '!']))