## Punto 1
def calcular_IMC(peso:int, altura:float) -> float:
  """función para calcular el IM de una persona, dado su peso en (kg) y su altura en (mts)"""
  return round(peso / (altura ** 2), 2)

## Punto 2
def calcular_bisiesto(year: int) -> bool:
  """determina si un año es bisiesto según las reglas establecidas."""
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
  return False

## Punto 3
def calcular_divisores(num1:int, num2:int) -> list:
  """función para calcular los divisores de dos números enteros positivos entre 1 y 100"""
  divisores = []

  for i in range(1, 101):
    if i % num1 == 0 and i % num2 == 0:
      divisores.append(i)
  
  return divisores

## Punto 4
def clasificar_palabras(palabras:list) -> dict:
  """función para clasificar las palabras de una lista de acuerdo a la cantidad de letras"""
  diccionario = {}

  for i in palabras:
    diccionario[i] = len(i)

  return diccionario

## LOS CASOS DE PRUEBA HAN SIDO GENERADOS POR IA PARA OBTENER LOS 
## RESULTADOS ESPERADOS CORRECTOS Y HACER LA DEBIDA COMPARACIÓN


print("\n - Punto 1:")
print(calcular_IMC(70, 1.75))  # 22.86  (Peso normal)
print(calcular_IMC(50, 1.60))  # 19.53  (Peso normal)
print(calcular_IMC(90, 1.75))  # 29.39  (Sobrepeso)
print(calcular_IMC(45, 1.50))  # 20.00  (Peso normal)
print(calcular_IMC(120, 1.80)) # 37.04  (Obesidad)

print("\n - Punto 2:")
print(calcular_bisiesto(2024))  # True  (divisible por 4 y no por 100)
print(calcular_bisiesto(1900))  # False (divisible por 100, pero no por 400)
print(calcular_bisiesto(2000))  # True  (divisible por 100 y por 400)
print(calcular_bisiesto(2023))  # False (no es divisible por 4)
print(calcular_bisiesto(2400))  # True  (divisible por 400)



print("\n - Punto 4:")
print(calcular_divisores(10, 3))  # [30, 60, 90]
print(calcular_divisores(5, 2))   # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(calcular_divisores(7, 3))   # [21, 42, 63, 84]
print(calcular_divisores(4, 6))   # [12, 24, 36, 48, 60, 72, 84, 96]
print(calcular_divisores(1, 50))  # [50, 100]
