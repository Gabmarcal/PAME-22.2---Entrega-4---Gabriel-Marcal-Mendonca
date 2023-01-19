from flask import request
from flask.views import MethodView

from .models import my_products as products

from .schemas import *

def get_last_id_products():
    last_product = products[-1]
    return last_product['id']
   
class ProductController_adm(MethodView):

    def post(self):
        
        schema = ProductSchema()
        data = request.json

        data['id'] = get_last_id_products() +1

        try:
            product = schema.dump(data)
            products.append(product)

        except:
            print("erro!")
            return{},400

        return product, 201
    
    def get(self):
        schema = ProductSchema()
        return schema.dump(products,many=True), 200

class ProductDetails_adm(MethodView):

    def get(self,id):
        schema = ProductSchema()

        for product in products:
            if product['id'] == id:
                return schema.dump(product), 200
        return {}, 404
    
    def put(self,id):
        schema = ProductSchema()
        data = request.json

        productindex = -1

        for product in products:
            if product['id'] == id:
                productindex = products.index(product)
            
        if productindex == -1:
            return{}, 404
        
        data['id'] = id
        new_product = schema.dump(data)
        products[productindex] = new_product
        return new_product
    
    def patch(self,id):
        schema = ProductSchema()
        data = request.json

        productindex = -1

        for product in products:
            if product['id'] == id:
                productindex = products.index(product)
            
        if productindex == -1:
            return{}, 404
        
        product = products[productindex]

        preco = data.get('preco', product['preco'])
        tipo = data.get('tipo', product['tipo'])
        tamanho = data.get('tamanho', product['tamanho'])
        cor = data.get('cor', product['cor'])
        quantidade = data.get('quantidade', product['quantidade'])

        data['preco'] = preco
        data['tipo'] = tipo
        data['tamanho'] = tamanho
        data['cor'] = cor
        data['quantidade'] = quantidade
        data['id'] = id

        product = schema.dump(data)
        products[productindex] = product

        return product, 201
    
    def delete(self,id):
        for product in products:
            if product['id'] == id:
                products.remove(product)
                return{}, 204
        return{}, 404

class ProductController_client(MethodView):

    def get(self):
        schema = ProductSchema()
        return schema.dump(products,many=True), 200

class ProductDetails_client(MethodView):

    def get(self,id):
        schema = ProductSchema()

        for product in products:
            if product['id'] == id:
                return schema.dump(product), 200
        return {}, 404
    
    