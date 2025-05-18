from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv
import os

from utils.test_runner import run_tests

from models.heladeria import Heladeria
from models.copa import Copa
from models.malteada import Malteada
from models.ingrediente import Ingrediente
from models.base import Base
from models.complemento import Complemento

# ---------------------------------- ENV ---------------------------------- #
load_dotenv()

user = os.getenv("USER")
password = os.getenv("PASSWORD")
connection = os.getenv("CONNECTION")

# ---------------------------------- APP ---------------------------------- #
app = Flask(__name__, template_folder='views')

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{user}:{password}@{connection}'
db = SQLAlchemy(app)

# -------------------------- MODELOS SQLALCHEMY --------------------------- #

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


# ---------------------------- CARGA MODELO ------------------------------ #

def cargar_desde_bd():
    ingredientes_db = IngredienteDB.query.all()
    ingredientes_dict = {}
    for ing in ingredientes_db:
        if ing.tipo == "Base":
            obj = Base(ing.nombre, ing.precio, ing.calorias, ing.inventario, ing.es_vegetariano, ing.sabor)
        else:
            obj = Complemento(ing.nombre, ing.precio, ing.calorias, ing.inventario, ing.es_vegetariano)
        ingredientes_dict[ing.id] = obj

    productos_db = ProductoDB.query.all()
    productos = []

    for p in productos_db:
        ing1 = ingredientes_dict[p.ingrediente1]
        ing2 = ingredientes_dict[p.ingrediente2]
        ing3 = ingredientes_dict[p.ingrediente3]

        if p.tipo == "Copa":
            producto = Copa(p.nombre, p.precio, p.tipo_vaso, ing1, ing2, ing3)
        else:  # Malteada
            producto = Malteada(p.nombre, p.precio, p.volumen, ing1, ing2, ing3)

        productos.append(producto)

    heladeria = Heladeria(*productos, list(ingredientes_dict.values()))
    return heladeria

# ------------------------------- RUTAS ---------------------------------- #
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/productos')
def productos():
    productos = heladeria.get_productos()
    return render_template('productos.html', productos=productos)

@app.route('/vender', methods=['GET', 'POST'])
def vendedor():
    mensaje = ""
    if request.method == 'POST':
        nombre_producto = request.form.get('producto', '')
        try:
            mensaje = heladeria.vender_producto(nombre_producto)
        except ValueError as e:
            mensaje = str(e)

    return render_template('vender.html', mensaje=mensaje)

@app.route('/tests')
def show_tests():
    output, success, tests = run_tests()
    return render_template('test.html', output=output, success=success, tests=tests)

# -------------------------- CREAR TABLAS -------------------------------- #

with app.app_context():
    db.create_all()
    heladeria = cargar_desde_bd()

# ----------------------------- RUN -------------------------------------- #

if __name__ == '__main__':
    app.run(debug=True)
