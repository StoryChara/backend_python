from circulo import area_circulo

def area_sombreada(lado:float) -> float:
    return (lado*lado) - area_circulo(lado/2)