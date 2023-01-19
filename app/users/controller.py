from flask import request
from flask.views import MethodView

from .models import my_users as users

from .schemas import *

def get_last_id_users():
    last_user = users[-1]
    return last_user['id']

class UserController_adm(MethodView):
    
    def post(self):
        schema = UserSchema()
        data = request.json

        data['id'] = get_last_id_users() +1

        if data['tipo'] != 'cliente' or 'administrador':
            print("erro!")
            return{}, 400

        try:
            user = schema.dump(data)
            users.append(user)

        except:
            print("erro!")
            return{}, 400
        
        return user, 201
    
    def get(self):
        schema=UserSchema()
        return schema.dump(users,many=True), 200

class UserDetails_adm(MethodView):

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

class UserDetails_client(MethodView):

    def get(self,id):
        schema = UserSchema()

        for user in users:
            if user['id'] == id:
                return schema.dump(user), 200
        return {}, 404
    
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

        data['username'] = username
        data['tipo'] = 'cliente'
        data['id'] = id

        user = schema.dump(data)
        users[userindex] = user

        return user, 201
