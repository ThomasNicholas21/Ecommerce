import os

class Config:     # Configuração da URI do banco de dados e outras configurações

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///meu_app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey')
