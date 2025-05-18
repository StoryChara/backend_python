from dotenv import load_dotenv
import os

load_dotenv(override=True)

class Config:
     SECRET_KEY = os.getenv("SECRET_KEY")
     SQLALCHEMY_DATABASE_URI = os.getenv("DB")