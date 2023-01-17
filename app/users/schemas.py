from app.extensions import ma

class UserSchema(ma.Schema):
    id = ma.Integer(dump_only=True)
    username = ma.String(required=True)
    tipo = ma.String(required=True)

class ProductSchema(ma.Schema):
    id = ma.Integer(dump_only=True)
    tipo = ma.String(required=True)
    preco = ma.Integer(required=True)
    tamanho = ma.String(required=True)
    quantidade = ma.Integer(required=True)

class CartSchema(ma.Schema):
    id = ma.Integer(dump_only=True)
    quantidade = ma.Integer(required=True)
    produtos = ma.List(required=True)