from app.extensions import ma
from app.products.schemas import ProductSchema

class CartSchema(ma.Schema):
    id = ma.Integer(dump_only=True)
    produtos = ma.List(ma.Nested(ProductSchema), required=True)