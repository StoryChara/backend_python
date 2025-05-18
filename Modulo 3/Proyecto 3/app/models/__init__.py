from app.config.db import db

class IngredienteDB(db.Model):
    __tablename__ = 'ingrediente'

    id = db.Column('idingrediente', db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    tipo = db.Column(db.Enum('Base', 'Complemento'), nullable=False)
    calorias = db.Column(db.Integer, nullable=False)
    inventario = db.Column(db.Float, nullable=False)
    es_vegetariano = db.Column(db.Boolean, nullable=False)
    sabor = db.Column(db.String(50), nullable=True)

class ProductoDB(db.Model):
    __tablename__ = 'producto'

    id = db.Column('idproductos', db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    tipo = db.Column(db.Enum('Malteada', 'Copa'), nullable=False)

    ingrediente1 = db.Column(db.Integer, db.ForeignKey('ingrediente.idingrediente'), nullable=False)
    ingrediente2 = db.Column(db.Integer, db.ForeignKey('ingrediente.idingrediente'), nullable=False)
    ingrediente3 = db.Column(db.Integer, db.ForeignKey('ingrediente.idingrediente'), nullable=False)

    volumen = db.Column(db.Float, nullable=True)
    tipo_vaso = db.Column(db.String(45), nullable=True)

    ing1 = db.relationship("IngredienteDB", foreign_keys=[ingrediente1])
    ing2 = db.relationship("IngredienteDB", foreign_keys=[ingrediente2])
    ing3 = db.relationship("IngredienteDB", foreign_keys=[ingrediente3])

from app.models.base import Base
from app.models.complemento import Complemento
from app.models.copa import Copa
from app.models.malteada import Malteada
from app.models.heladeria import Heladeria

def crear_heladeria():
    ingredientes_db = IngredienteDB.query.all()
    ingredientes_dict = {}
    for ing in ingredientes_db:
        if ing.tipo == "Base":
            obj = Base(ing.id, ing.nombre, ing.precio, ing.calorias, ing.inventario, ing.es_vegetariano, ing.sabor)
        else:
            obj = Complemento(ing.id, ing.nombre, ing.precio, ing.calorias, ing.inventario, ing.es_vegetariano)
        ingredientes_dict[ing.id] = obj

    productos_db = ProductoDB.query.all()
    productos = []

    for p in productos_db:
        ing1 = ingredientes_dict[p.ingrediente1]
        ing2 = ingredientes_dict[p.ingrediente2]
        ing3 = ingredientes_dict[p.ingrediente3]

        if p.tipo == "Copa":
            producto = Copa(p.id, p.nombre, p.precio, p.tipo_vaso, ing1, ing2, ing3)
        else:  # Malteada
            producto = Malteada(p.id, p.nombre, p.precio, p.volumen, ing1, ing2, ing3)

        productos.append(producto)

    heladeria = Heladeria(*productos, list(ingredientes_dict.values()))
    return heladeria