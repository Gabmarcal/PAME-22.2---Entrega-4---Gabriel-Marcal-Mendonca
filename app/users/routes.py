from flask import Blueprint
from .controller import *

user_api = Blueprint("user_api","__name__")

#users
user_api.add_url_rule(

    "/users",
    view_func=UserController.as_view("users_controller"),
    methods = ['POST','GET']
)

#users/id
user_api.add_url_rule(

    "/users/<int:id>",
    view_func=UserDetails.as_view("users_details"),
    methods = ['GET','PUT','PATCH','DELETE']
)

#products
user_api.add_url_rule(

    "/products",
    view_func=ProductController.as_view("products_controller"),
    methods = ['POST','GET']
)

#products/id
user_api.add_url_rule(

    "/products/<int:id>",
    view_func=ProductDetails.as_view("product_details"),
    methods = ['GET','PUT','PATCH','DELETE']
)

#