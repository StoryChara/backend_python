from flask import Flask

from app.config.auth import login_manager
from app.config.db import db
from app.config.routes import registrar_rutas

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
     
     return app
