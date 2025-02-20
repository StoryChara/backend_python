from circulo import area_circulo

def area_sombreada(lado:float) -> float:
    """funcion que retorna el area sombreada de un cuadrado con un circulo en su interior"""
    return round((lado**2) - area_circulo(lado/2), 2)