from modulo import area_sombreada

try:
  lado = int(input("Hola! Por favor ingresa el lado del cuadrado \n >> "))
  print(f"El resultado del area sombreada es: {'{:.2f}'.format(area_sombreada(lado))}")
except:
  print("Debes ingresar un entero")