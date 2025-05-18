from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required

from app.models.user import Usuario
from app.config.auth import login_manager

from app.models.db import Perro, Guarderia, Cuidador

home_blueprint = Blueprint("home", __name__)

@login_manager.user_loader
def load_user(user_id:int) -> Usuario:
     return Usuario.query.get(user_id)

@home_blueprint.route("/", methods = ["GET"])
def home():
     return render_template('index.html')

@home_blueprint.route('/dashboard')
@login_required
def dashboard():
     aut = current_user.es_admin
     return render_template('dashboard.html', autorizacion=aut)

@home_blueprint.route('/login', methods = ["GET", "POST"])
def auth():

     if request.method == 'GET':
          return render_template("login.html")

     username = request.form.get('username')
     password = request.form.get('password')

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
@login_required
def catalogo():
     if current_user.es_admin == True:
          perros = Perro.query.all()
          info_perros = [{
               "nombre": perro.Nombre,
               "raza": perro.Raza,
               "peso": perro.Peso,
               "edad": perro.Edad
          } for perro in perros]
          return render_template('catalogo.html', perros=info_perros)
     else:
          flash("No tienes permisos para acceder a este recurso.", "danger")
          return redirect(url_for('home.dashboard'))

@home_blueprint.route('/logout')
def logout():
     logout_user()
     return redirect(url_for('home.home'))