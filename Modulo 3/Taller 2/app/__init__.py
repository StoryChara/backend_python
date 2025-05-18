from flask import Flask

from app.config.routes import registrar_rutas

def create_app() -> Flask:
     app = Flask(__name__, template_folder='views')

     ## WEBSITE -------------------------------- ##

     registrar_rutas(app)
     
     return app
