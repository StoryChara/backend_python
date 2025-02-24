from circulo import area_circulo

def area_cuadrado(lado:float) -> float:
    """funcion que retorna el area de un cuadrado dado su lado"""
    return lado**2

def area_sombreada(lado:float) -> float:
    """funcion que retorna el area sombreada de un cuadrado con un circulo en su interior"""
    return round(area_cuadrado(lado) - area_circulo(lado/2), 2)