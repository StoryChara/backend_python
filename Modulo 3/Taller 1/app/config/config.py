from dotenv import load_dotenv
import os

load_dotenv(override=True)

class Config:
     SECRET_KEY = os.getenv("SECRET_KEY")
     SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{os.getenv("USER")}:{os.getenv("PASSWORD")}@{os.getenv("CONNECTION")}'