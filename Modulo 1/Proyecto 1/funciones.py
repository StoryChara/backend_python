def es_sano(calorias: int, vegetariano: bool) -> bool:
    """Determina si un ingrediente es sano. Un ingrediente es sano si tiene menos de 100 calorías o si es vegetariano."""
    return calorias < 100 or vegetariano

def contar_calorias(ingredientes_calorias: list[int]) -> float:
    """Calcula el conteo total de calorías de un producto, aplicando un factor de reducción del 5%."""
    return round(sum(ingredientes_calorias) * 0.95, 2)

def calcular_costo(ingrediente1: dict[str, float], ingrediente2: dict[str, float], ingrediente3: dict[str, float]) -> float:
    """Calcula el costo total de producción de un producto sumando los precios de los tres ingredientes."""
    return round(ingrediente1["precio"] + ingrediente2["precio"] + ingrediente3["precio"], 2)

def calcular_rentabilidad(precio_venta: float, ingrediente1: dict[str, float], ingrediente2: dict[str, float], ingrediente3: dict[str, float]) -> float:
    """Calcula la rentabilidad de un producto restando su costo de producción al precio de venta."""
    return round(precio_venta - calcular_costo(ingrediente1, ingrediente2, ingrediente3), 2)

def producto_mas_rentable(producto1: dict[str, float], producto2: dict[str, float], producto3: dict[str, float], producto4: dict[str, float]) -> str:
    """Encuentra el producto con mayor rentabilidad y retorna su nombre."""
    productos = [producto1, producto2, producto3, producto4]
    producto_mayor_rentabilidad = max(productos, key=lambda p: p["rentabilidad"])
    return producto_mayor_rentabilidad["nombre"]