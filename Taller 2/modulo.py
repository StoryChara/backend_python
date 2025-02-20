from circulo import area_circulo

def area_sombreada(lado:float) -> float:
    return (lado**2) - area_circulo(lado/2)