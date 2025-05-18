from flask import Blueprint, render_template, request, jsonify, abort
from app.models import Cat, Dog, Ferret, Snake

import requests

url_api = 'http://127.0.0.1:5000/api'

home_blueprint = Blueprint("home", __name__)

@home_blueprint.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template('index.html', message='Esperando consulta.')
    
    animal = request.form.get('animal')
    response = requests.get(f"http://127.0.0.1:5000/api/",  params={"animal": animal})
    if response.status_code == 200:
        return render_template('index.html', message=response.json())
    else:
        abort(404)
    

@home_blueprint.route("/api/", methods=["GET"])
def api():
    animal = request.args.get('animal')
    if animal == 'gato':
        return jsonify(Cat.get_json()), 200
    elif animal == 'perro':
        return jsonify(Dog.get_json()), 200
    elif animal == 'huron':
        return jsonify(Ferret.get_json()), 200
    elif animal == 'boa':
        return jsonify(Snake.get_json()), 200
    else:
        return jsonify({
            "animal": animal,
            "sonido": None,
            "mensaje": "Animal no encontrado"
        }), 404