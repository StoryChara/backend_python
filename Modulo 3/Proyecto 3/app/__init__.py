from flask import Flask

from app.config.auth import login_manager
from app.config.db import db
from app.config.routes import registrar_rutas
from app.models import crear_heladeria

from flask import render_template

def create_app(config) -> Flask:
     app = Flask(__name__, template_folder='views')
     app.config.from_object(config)

     ## LOGIN --------------------------------------- ##

     login_manager.init_app(app)

     ## SQL ------------------------------------------- ##

     db.init_app(app)

     ## WEBSITE -------------------------------- ##

     registrar_rutas(app)

     with app.app_context():
          db.create_all()
          app.config['heladeria'] = crear_heladeria()

     
     ## ERRORES ------------------------------------- ##

     @app.errorhandler(401)
     def forbidden_error(error):
          return render_template('401.html'), 401
     
     @app.errorhandler(404)
     def forbidden_error(error):
          return render_template('404.html'), 404
     
     return app
