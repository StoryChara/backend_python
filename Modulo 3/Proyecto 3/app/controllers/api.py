from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app, jsonify, abort
from flask_login import current_user, login_user, logout_user, login_required

from functools import wraps

from app.models.heladeria import Heladeria
from app.models.iproducto import IProducto
from app.models.ingrediente import Ingrediente


api_blueprint = Blueprint("api", __name__, url_prefix="/api")


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.es_admin:
            abort(401)
        return f(*args, **kwargs)
    return decorated_function

def empleado_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not (current_user.es_empleado or current_user.es_admin):
            abort(401)
        return f(*args, **kwargs)
    return decorated_function

def cliente_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated: 
            abort(401)
        return f(*args, **kwargs)
    return decorated_function




@api_blueprint.route("/", methods=["GET"])
def api():
    return jsonify({"message": "Welcome to the API!"}), 200

@api_blueprint.route("/productos/", methods=["GET"])
def get_productos():
    heladeria: Heladeria = current_app.config['heladeria']
    productos = heladeria.get_productos_API_PUBLIC()
    return jsonify(productos), 200

@api_blueprint.route("/productos/R/", methods=["GET"])
@cliente_required
def get_productos_R():
    heladeria: Heladeria = current_app.config['heladeria']
    productos = heladeria.get_productos_API_CLIENTE()
    return jsonify(productos), 200

@api_blueprint.route("/producto/ID/", methods=["GET"])
@cliente_required
def get_producto_by_id():
    id = int(request.args.get("id"))
    heladeria: Heladeria = current_app.config['heladeria']
    producto: IProducto = heladeria.search_producto_ID(id)
    
    if producto is None:
        return jsonify({"error": "Producto no encontrado"}), 404
    else:
        return jsonify(producto.to_dict_API_CLIENTE()), 200
    
@api_blueprint.route("/producto/name/", methods=["GET"])
@cliente_required
def get_producto_by_name():
    nombre = request.args.get("nombre", "")
    heladeria: Heladeria = current_app.config['heladeria']
    producto = heladeria.search_producto_NAME(nombre)
    
    if producto is None:
        return jsonify({"error": "Producto no encontrado"}), 404
    else:
        return jsonify(producto.to_dict_API_CLIENTE()), 200
    
@api_blueprint.route("/producto/ID/calories/", methods=["GET"])
@cliente_required
def get_producto_calories_by_id():
    id = int(request.args.get("id"))
    heladeria: Heladeria = current_app.config['heladeria']
    producto: IProducto = heladeria.search_producto_ID(id)
    
    if producto is None:
        return jsonify({"error": "Producto no encontrado"}), 404
    else:
        info = producto.to_dict_API_CLIENTE()
        return jsonify({
            "id": info["id"],
            "nombre": info["nombre"],
            "calorias": info["calorias"]
        }), 200
    
@api_blueprint.route("/producto/ID/rent/", methods=["GET"])
@admin_required
def get_producto_rent_by_id():
    id = int(request.args.get("id"))
    heladeria: Heladeria = current_app.config['heladeria']
    producto: IProducto = heladeria.search_producto_ID(id)

    if producto is None:
        return jsonify({"error": "Producto no encontrado"}), 404
    else:
        info = producto.to_dict_API_FINANCE()
        return jsonify({
            "id": info["id"],
            "nombre": info["nombre"],
            "rentabilidad": info["rentabilidad"]
        }), 200
    
@api_blueprint.route("/producto/ID/costo/", methods=["GET"])
@admin_required
def get_producto_costo_by_id():
    id = int(request.args.get("id"))
    heladeria: Heladeria = current_app.config['heladeria']
    producto: IProducto = heladeria.search_producto_ID(id)

    if producto is None:
        return jsonify({"error": "Producto no encontrado"}), 404
    else:
        info = producto.to_dict_API_FINANCE()
        return jsonify({
            "id": info["id"],
            "nombre": info["nombre"],
            "costo": info["costo"]
        }), 200
    
@api_blueprint.route("/producto/ID/venta/", methods=["GET"])
@cliente_required
def get_producto_venta_by_id():
    id = int(request.args.get("id"))
    heladeria: Heladeria = current_app.config['heladeria']
    
    try:
        mensaje = heladeria.vender_producto_ID(id)
        return jsonify({ "mensaje": mensaje }), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400



@api_blueprint.route("/ing/", methods=["GET"])
def get_ingredientes():
    heladeria: Heladeria = current_app.config['heladeria']
    ingredientes = heladeria.get_ingredientes_API_PUBLIC()
    return jsonify(ingredientes), 200

@api_blueprint.route("/ing/R/", methods=["GET"])
@cliente_required
def get_ingredientes_R():
    heladeria: Heladeria = current_app.config['heladeria']
    ingredientes = heladeria.get_ingredientes_API_CLIENTE()
    return jsonify(ingredientes), 200

@api_blueprint.route("/ing/ID/", methods=["GET"])
@cliente_required
def get_ing_by_id():
    id = int(request.args.get("id"))
    heladeria: Heladeria = current_app.config['heladeria']
    ingrediente: Ingrediente = heladeria.search_ingrediente_ID(id)
    
    if ingrediente is None:
        return jsonify({"error": "Producto no encontrado"}), 404
    else:
        return jsonify(ingrediente.to_dict_API_CLIENTE()), 200
    
@api_blueprint.route("/ing/name/", methods=["GET"])
@cliente_required
def get_ing_by_name():
    nombre = request.args.get("nombre", "")
    heladeria: Heladeria = current_app.config['heladeria']
    ingrediente: Ingrediente = heladeria.search_ingrediente_NAME(nombre)
    
    if ingrediente is None:
        return jsonify({"error": "Producto no encontrado"}), 404
    else:
        return jsonify(ingrediente.to_dict_API_CLIENTE()), 200
    
@api_blueprint.route("/ing/ID/sano/", methods=["GET"])
@cliente_required
def get_ing_sano_by_id():
    id = int(request.args.get("id"))
    heladeria: Heladeria = current_app.config['heladeria']
    ingrediente: Ingrediente = heladeria.search_ingrediente_ID(id)
    
    if ingrediente is None:
        return jsonify({"error": "Producto no encontrado"}), 404
    else:
        info = ingrediente.to_dict_API_CLIENTE()
        return jsonify({
            "id": info["id"],
            "nombre": info["nombre"],
            "calorias": info["calorias"],
            "es_vegetariano": info["es_vegetariano"],
            "es_sano": info["es_sano"]
        }), 200
    
    
@api_blueprint.route("/ing/ID/abastecer/", methods=["GET"])
@empleado_required
def abastecer_ing_by_id():
    id = int(request.args.get("id"))
    heladeria: Heladeria = current_app.config['heladeria']
    ingrediente: Ingrediente = heladeria.search_ingrediente_ID(id)

    if ingrediente is None:
        return jsonify({"error": "Producto no encontrado"}), 404
    else:
        ingrediente.abastecer()
        return jsonify({"message": "Producto abastecido exitosamente"}), 200
    
@api_blueprint.route("/ing/ID/renovar/", methods=["GET"])
@empleado_required
def renovar_ing_by_id():
    id = int(request.args.get("id"))
    cantidad = float(request.args.get("cantidad"))
    heladeria: Heladeria = current_app.config['heladeria']
    ingrediente: Ingrediente = heladeria.search_ingrediente_ID(id)

    if ingrediente is None:
        return jsonify({"error": "Producto no encontrado"}), 404
    else:
        ingrediente.renovar_inventario(cantidad)
        return jsonify({"message": "Producto renovado exitosamente"}), 200