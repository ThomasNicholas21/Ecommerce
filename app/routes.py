from flask import Flask
from .models import db
from .controllers.user_controller import user_bp
from .controllers.product_controller import product_bp
from .controllers.order_controller import order_bp

def create_app(config_class): # Função para criar a aplicação Flask e configurar as rotas e o banco de dados

    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

        # Registro dos blueprints das rotas

    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(product_bp, url_prefix='/api')
    app.register_blueprint(order_bp, url_prefix='/api')

    return app
