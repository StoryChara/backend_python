from flask import Flask, render_template
from models.controller import Controller

app = Flask(__name__)
controller = Controller()

@app.route("/")
def index():
     perros = controller.retornar_perros()
     info_perros = []

     for perro in perros:
          info_perros.append({  # ✅ Agregar cada perro a la lista
            "nombre": perro.get_nombre(),
            "raza": perro.get_raza(),
            "peso": perro.get_peso(),
            "edad": perro.get_edad()
          })

     return render_template('index.html', perros = info_perros)

if __name__ == '__main__':
     app.run(debug=True)