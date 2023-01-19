from flask import request
from flask.views import MethodView

from .models import my_carts as carts
from app.products.models import my_products as products

from .schemas import *

class Cart_adm(MethodView):
    
    def post(self,id):
        schema = CartSchema()
        data = request.json

        data['id'] = id
        data['produtos'] = []

        try:
            cart = schema.dump(data)
            carts.append(cart)

        except:
            print("erro!")
            return{},400

        return cart, 201 

    def get(self,id):
        schema = CartSchema()

        for cart in carts:
            if cart['id'] == id:
                return schema.dump(cart), 200
        return {}, 404
    
    def delete(self,id):
        for cart in carts:
            if cart['id'] == id:
                carts.remove(cart)
        return{}, 404
    
class Cart_client(MethodView):

    def get(self,id):
        schema = CartSchema()

        for cart in carts:
            if cart['id'] == id:
                return schema.dump(cart), 200
        return {}, 404

class Cart_adding(MethodView):

    def patch(self,cart_id,product_id):
        cartindex = -1

        for cart in carts:
            if cart['id'] == cart_id:
                cartindex = carts.index(cart)
            
        if cartindex == -1:
            return{}, 404
        
        cart = carts[cartindex]

        for product in products:
            if product['id'] == product_id:
                produto = product

        produtos = cart['produtos']
        produtos.append(produto)

        cart['produtos'] = produtos
        cart['id'] = cart_id

        carts[cartindex] = cart

        return cart, 201

class Cart_buying(MethodView):
    
    def patch(self,id):
        cartindex = -1

        total_value = 0

        for cart in carts:
            if cart['id'] == id:
                cartindex = carts.index(cart)
            
        if cartindex == -1:
            return{}, 404
        
        cart = carts[cartindex]
        produtos = cart['produtos']
        
        for produto in produtos:

            if produto['quantidade'] == 0: return {}, 400

            produto['quantidade'] -= 1
            total_value += produto['preco']

        cart['id'] = id
        cart['produtos'] = []

        carts[cartindex] = cart

        return cart, 201

