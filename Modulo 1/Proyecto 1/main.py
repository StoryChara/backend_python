## ESTE EJEMPLO FUE CREADO CON IA PARA UNA MAYOR FACILIDAD Y PODER COMPARAR DE FORMA OPTIMA CON EL RESULTADO ESPERADO

from base import Base
from complemento import Complemento
from copa import Copa
from malteada import Malteada
from heladeria import Heladeria

# Crear ingredientes (bases y complementos)
helado_fresa = Base("Helado de Fresa", 1200, 150, 10, True, "Fresa")
chispas_chocolate = Complemento("Chispas de Chocolate", 500, 50, 10, True)
mani_japones = Complemento("Maní Japonés", 900, 200, 10, False)

helado_vainilla = Base("Helado de Vainilla", 1300, 140, 10, True, "Vainilla")
sirope_caramelo = Complemento("Sirope de Caramelo", 600, 80, 15, True)
nueces = Complemento("Nueces", 800, 180, 12, True)

# Crear productos (copas y malteadas)
copa_fresa = Copa("Copa Samurai", 7500, "Cristal", helado_fresa, chispas_chocolate, mani_japones)
malteada_choco = Malteada("Malteada Chocoespacial", 8500, 500, helado_fresa, chispas_chocolate, mani_japones)
copa_vainilla = Copa("Copa Dulce Encanto", 7800, "Vidrio", helado_vainilla, sirope_caramelo, nueces)
malteada_caramelo = Malteada("Malteada Caramelada", 8200, 500, helado_vainilla, sirope_caramelo, nueces)

# Crear la heladería con los productos y el inventario
mi_heladeria = Heladeria(copa_fresa, malteada_choco, copa_vainilla, malteada_caramelo, 
                         [helado_fresa, chispas_chocolate, mani_japones, helado_vainilla, sirope_caramelo, nueces])

# Mostrar el producto más rentable
print(f"🔝 Producto más rentable: {mi_heladeria.producto_mas_rentable()}")

# Intentar vender productos
print("\n💰 Intentando vender productos...")
mi_heladeria.vender_producto("Copa Samurai")
mi_heladeria.vender_producto("Malteada Chocoespacial")
mi_heladeria.vender_producto("Copa Dulce Encanto")
mi_heladeria.vender_producto("Malteada Caramelada")

# Mostrar contador de ventas
print(f"\n📊 Ventas totales del día: {mi_heladeria.get_contador_ventas()}")