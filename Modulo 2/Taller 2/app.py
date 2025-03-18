from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

app = Flask(__name__, template_folder='views')

## ENV ----------------------------------------- ##
load_dotenv()

user = os.getenv("USER")
password = os.getenv("PASSWORD")
connection = os.getenv("CONNECTION")

## SQL ------------------------------------------- ##

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{user}:{password}@{connection}'
db = SQLAlchemy(app)

## CLASES ---------------------------------------- ##

class Guarderia(db.Model):
    __tablename__ = 'GUARDERIAS'
    ID_Guarderia = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Nombre = db.Column(db.String(45), nullable=False)
    Direccion = db.Column(db.String(100), nullable=False)
    Telefono = db.Column(db.String(20), nullable=False)

class Cuidador(db.Model):
    __tablename__ = 'CUIDADOR'
    ID_Cuidador = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Nombre = db.Column(db.String(45), nullable=False)
    Telefono = db.Column(db.String(20), nullable=False)

class Perro(db.Model):
    __tablename__ = 'PERRO'
    ID_Perro = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Nombre = db.Column(db.String(45), nullable=False)
    Raza = db.Column(db.String(45), nullable=False)
    Edad = db.Column(db.Integer, nullable=False)
    Peso = db.Column(db.Numeric(10, 2), nullable=False)

## WEBSITE -------------------------------- ##

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/catalogo")
def index():
    perros = Perro.query.all()
    info_perros = [{
        "nombre": perro.Nombre,
        "raza": perro.Raza,
        "peso": perro.Peso,
        "edad": perro.Edad
    } for perro in perros]
    return render_template('catalogo.html', perros=info_perros)

@app.route("/punto_5")
def punto_5():
    lassie_dogs = Perro.query.filter_by(Nombre="Lassie").all()

    id_mario = Cuidador.query.filter_by(Nombre="Mario").first()
    perros_mario = Perro.query.filter(Perro.Peso<3).all()
    return render_template('punto_5.html', lassie=len(lassie_dogs), mario=id_mario, perros=perros_mario)

if __name__ == '__main__':
    app.run(debug=True)