from app.config.db import db

class Guarderia(db.Model):
     __tablename__ = 'GUARDERIAS'
     ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
     Nombre = db.Column(db.String(45), nullable=False)
     Direccion = db.Column(db.String(100), nullable=False)
     Telefono = db.Column(db.String(20), nullable=False)
     cuidadores = db.relationship('Cuidador', backref='guarderia', lazy=True)
     perros = db.relationship('Perro', backref='guarderia', lazy=True)

class Cuidador(db.Model):
     __tablename__ = 'CUIDADORES'
     ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
     Nombre = db.Column(db.String(45), nullable=False)
     Telefono = db.Column(db.String(20), nullable=False)
     ID_GUARDERIA = db.Column(db.Integer, db.ForeignKey('GUARDERIAS.ID'), nullable=False)
     perros = db.relationship('Perro', backref='cuidador', lazy=True)

class Perro(db.Model):
     __tablename__ = 'PERROS'
     ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
     Nombre = db.Column(db.String(45), nullable=False)
     Raza = db.Column(db.String(45), nullable=False)
     Edad = db.Column(db.Integer, nullable=False)
     Peso = db.Column(db.Numeric(10, 2), nullable=False)
     ID_GUARDERIA = db.Column(db.Integer, db.ForeignKey('GUARDERIAS.ID'), nullable=False)
     ID_CUIDADOR = db.Column(db.Integer, db.ForeignKey('CUIDADORES.ID'), nullable=False)