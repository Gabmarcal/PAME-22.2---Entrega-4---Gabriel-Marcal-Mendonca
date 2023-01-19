from flask import Blueprint
from .controller import *

user_api = Blueprint("user_api",__name__)

#/users_adm
user_api.add_url_rule(

    "/users_adm",
    view_func=UserController_adm.as_view("users_controller_adm"),
    methods = ['POST','GET']
)

#/users_adm/id
user_api.add_url_rule(

    "/users_adm/<int:id>",
    view_func=UserDetails_adm.as_view("users_details_adm"),
    methods = ['GET','PUT','PATCH','DELETE']
)

#/users_client/id
user_api.add_url_rule(

    "/users_client/<int:id>",
    view_func=UserDetails_client.as_view("users_details_client"),
    methods = ['GET','PATCH']
)