from flask import Flask
from app.users.routes import user_api
from app.products.routes import product_api
from app.carts.routes import cart_api

def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_api)
    app.register_blueprint(product_api)
    app.register_blueprint(cart_api)
    return app
