from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app, abort
from flask_login import current_user, login_user, logout_user, login_required

from functools import wraps

import requests

from app.models.user import Usuario
from app.config.auth import login_manager

url_api = 'http://127.0.0.1:5000/api'

home_blueprint = Blueprint("home", __name__)

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

@login_manager.user_loader
def load_user(user_id:int) -> Usuario:
     return Usuario.query.get(user_id)

@home_blueprint.route("/", methods = ["GET"])
def home():
     active = current_user.is_authenticated
     return render_template('index.html', user=active)

@home_blueprint.route('/dashboard')
@login_required
def dashboard():
     return render_template('dashboard.html', usuario=current_user)

@home_blueprint.route('/login', methods = ["GET", "POST"])
def auth():
     if request.method == 'GET':
          return render_template("login.html")

     username = request.form.get('username'); password = request.form.get('password')
     usuario = Usuario.query.filter_by(Username=username, Password=password).first()

     if usuario:
          login_user(usuario)
          return redirect(url_for('home.dashboard'))
     else:
          flash("Las credenciales son incorrectas.", "danger")
          return redirect(url_for('home.auth'))
     
@home_blueprint.route('/auth/profile')
@login_required
def profile():
     return render_template("profile.html", usuario=current_user)

@home_blueprint.route("/catalogo")
def catalogo():
     if current_user.is_authenticated:
          response = requests.get(f"{url_api}/productos/R/", cookies=request.cookies)
     else:
          response = requests.get(f"{url_api}/productos/")

     data = response.json() if response.status_code == 200 else abort(404)

     return render_template("catalogo.html", productos=data)

@home_blueprint.route('/logout')
def logout():
     logout_user()
     return redirect(url_for('home.home'))

@home_blueprint.route('/finanza', methods=["GET", "POST"])
@admin_required
def finanza():
     if request.method == 'GET':
          return render_template("finanza.html", rentabilidad={}, costo={}, message="Esperando ID.")
     
     id = request.form.get('id')
     rentabilidad = requests.get(f"{url_api}/producto/ID/rent/",  params={"id": id}, cookies=request.cookies)
     costos = requests.get(f"{url_api}/producto/ID/costo/",  params={"id": id}, cookies=request.cookies)

     if rentabilidad.status_code == 200 and costos.status_code == 200:
          rent = rentabilidad.json()
          cost = costos.json()
          return render_template("finanza.html", rentabilidad=rent, costo=cost, message="Exito.")
     elif rentabilidad.status_code == 404 or costos.status_code == 404:
          return render_template("finanza.html", rentabilidad={}, costo={}, message="Elemento NO encontrado.")
     else:
          abort(404)

@home_blueprint.route('/buscar', methods=["GET", "POST"])
@cliente_required
def buscar():
     if request.method == 'GET':
          return render_template("buscar.html", message='Esperando Parámetros.', data={}, type='')
     
     objeto = request.form.get("objeto")
     opcion = request.form.get("opcion")
     producto = request.form.get("producto")

     if objeto == "prod":
          if opcion == "id":
               resultados = requests.get(f"{url_api}/producto/ID/",  params={"id": int(producto)}, cookies=request.cookies)
          elif opcion == "name":
               resultados = requests.get(f"{url_api}/producto/name/",  params={"nombre": producto}, cookies=request.cookies)
          else:
               abort(404)
     elif objeto == "ing":
          if opcion == "id":
               resultados = requests.get(f"{url_api}/ing/ID/",  params={"id": int(producto)}, cookies=request.cookies)
          elif opcion == "name":
               resultados = requests.get(f"{url_api}/ing/name/",  params={"nombre": producto}, cookies=request.cookies)
          else:
               abort(404)
     else:
          abort(404)
     
     if resultados.status_code == 200:
          data = resultados.json()
          return render_template("buscar.html", message="Exito.", resultados=data, type=objeto)
     elif resultados.status_code == 404:
          return render_template("buscar.html", message="Elemento NO encontrado.", resultados={}, type='')
     else:
          abort(404)

@home_blueprint.route("/ingredientes")
@empleado_required
def ingredientes():
     response = requests.get(f"{url_api}/ing/R/", cookies=request.cookies)

     data = response.json() if response.status_code == 200 else abort(404)

     return render_template("ingredientes.html", productos=data)

@home_blueprint.route("/calorias", methods=["GET", "POST"])
@empleado_required
def calorias():
     if request.method == 'GET':
          return render_template("calorias.html", message='Esperando ID.', data={}, type='')
     
     objeto = request.form.get("objeto")
     id = int(request.form.get("id"))

     if objeto == "prod":
          resultados = requests.get(f"{url_api}/producto/ID/calories/",  params={"id": id}, cookies=request.cookies)
     elif objeto == "ing":
          resultados = requests.get(f"{url_api}/ing/ID/sano/",  params={"id": id}, cookies=request.cookies)
     else:
          abort(404)
     
     if resultados.status_code == 200:
          data = resultados.json()
          return render_template("calorias.html", message="Exito.", resultados=data, type=objeto)
     elif resultados.status_code == 404:
          return render_template("calorias.html", message="Elemento NO encontrado.", resultados={}, type='')
     else:
          abort(404)

@home_blueprint.route("/vender", methods=["GET", "POST"])
@cliente_required
def vender():
     if request.method == 'GET':
          return render_template("venta.html", message='Esperando ID.', data={})
     
     id = int(request.form.get("id"))
     resultados = requests.get(f"{url_api}/producto/ID/venta/", params={"id": id}, cookies=request.cookies)

     if resultados.status_code == 200:
          data = resultados.json()
          return render_template("venta.html", message="Exito.", resultados=data)
     elif resultados.status_code == 400:
          data = resultados.json()
          return render_template("venta.html", message="Error en la solicitud.", resultados=data)
     else:
          abort(404)

@home_blueprint.route("/inventario", methods=["GET", "POST"])
@empleado_required
def inventario():
     if request.method == 'GET':
          return render_template("inv.html", message='Esperando ID.', resultados={})
     
     id = int(request.form.get("id"))
     opcion = request.form.get("opcion")
     cant = request.form.get("cantidad")

     if opcion == "abastecer":
          resultados = requests.get(f"{url_api}/ing/ID/abastecer/", params={"id": id}, cookies=request.cookies)
     elif opcion == "renovar":
          resultados = requests.get(f"{url_api}/ing/ID/renovar/", params={"id": id, "cantidad": int(cant)}, cookies=request.cookies)
     else:
          abort(404)
     
     if resultados.status_code == 200:
          data = resultados.json()
          return render_template("inv.html", message="Exito.", resultados=data)
     elif resultados.status_code == 404:
          data = resultados.json()
          return render_template("inv.html", message="Error en la solicitud.", resultados=data)
     else:
          abort(404)