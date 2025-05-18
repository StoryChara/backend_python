from app.controllers.home_controller import home_blueprint
from app.controllers.api import api_blueprint
from app.controllers.errors import error_blueprint
from app.controllers.api_test import Tapi_blueprint

def registrar_rutas(app):
     app.register_blueprint(home_blueprint)
     app.register_blueprint(api_blueprint)
     #app.register_blueprint(Tapi_blueprint)
     app.register_blueprint(error_blueprint)
