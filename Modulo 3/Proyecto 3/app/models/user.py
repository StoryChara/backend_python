from flask_login import UserMixin
from app.config.db import db
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(UserMixin, db.Model):
     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
     Username = db.Column(db.String(120), nullable=False)
     Password = db.Column(db.String(255), nullable=False)
     es_admin = db.Column(db.Boolean, nullable=False)
     es_empleado = db.Column(db.Boolean, nullable=False)

     def __init__(self, contraseña:str):
          self.Password = generate_password_hash(contraseña)

     def check_password(self, contraseña):
          return check_password_hash(self.Password, contraseña)
