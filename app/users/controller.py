from flask import request
from flask.views import MethodView

from .models import my_users as users
from .models import my_products as products
from .models import my_cart as carts

from .schemas import *

def get_last_id_users():
    last_user = users[-1]
    return last_user['id']

def get_last_id_products():
    last_product = products[-1]
    return last_product['id']

class UserController(MethodView):
     
    def post(self):
        schema = UserSchema()
        data = request.json

        data['id'] = get_last_id_users() +1

        try:
            user = schema.dump(data)
            users.append(user)

        except:
            print("erro!")
            return{},400
        
        return user, 201
    
    def get(self):
        schema=UserSchema()
        return schema.dump(users,many=True), 200

class UserDetails(MethodView):
    
    def get(self,id):
        schema = UserSchema()

        for user in users:
            if user['id'] == id:
                return schema.dump(user), 200
        return {}, 404
    
    def put(self,id):
        schema = UserSchema()
        data = request.json

        userindex = -1

        for user in users:
            if user['id'] == id:
                userindex = users.index(user)
            
        if userindex == -1:
            return{}, 404
        
        data['id'] = id
        new_user = schema.dump(data)
        users[userindex] = new_user
        return new_user
    
    def patch(self,id):
        schema = UserSchema()
        data = request.json

        userindex = -1

        for user in users:
            if user['id'] == id:
                userindex = users.index(user)
            
        if userindex == -1:
            return{}, 404
        
        user = users[userindex]

        username = data.get('username', user['username'])
        tipo = data.get('tipo', user['tipo'])

        data['username'] = username
        data['tipo'] = tipo
        data['id'] = id

        user = schema.dump(data)
        users[userindex] = user

        return user, 201
    
    def delete(self,id):
        for user in users:
            if user['id'] == id:
                users.remove(user)
                return{}, 204
        return{}, 404
    
class ProductController(MethodView):

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

class ProductDetails(MethodView):

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
        users[productindex] = new_product
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
        quantidade = data.get('quantidade', product['quantidade'])

        data['preco'] = preco
        data['tipo'] = tipo
        data['tamanho'] = tamanho
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

class Cart(MethodView):
    
    def post(self):
        schema = CartSchema()
        data = request.json

        data['id'] = get_last_id_users() + 1

        try:
            for num in range(data['id']): pass
        #Criando codigo

        except:
            print("erro!")
            return{},400
        
        return {}, 201
