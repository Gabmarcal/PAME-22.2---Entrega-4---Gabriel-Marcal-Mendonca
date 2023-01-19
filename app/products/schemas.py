from app.extensions import ma

class ProductSchema(ma.Schema):
    id = ma.Integer(dump_only=True)
    tipo = ma.String(required=True)
    preco = ma.Integer(required=True)
    tamanho = ma.String(required=True)
    cor = ma.String(required=True)
    quantidade = ma.Integer(required=True)

