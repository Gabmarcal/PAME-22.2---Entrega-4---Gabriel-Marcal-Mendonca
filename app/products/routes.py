from flask import Blueprint
from .controller import *

product_api = Blueprint("product_api",__name__)

#products_adm
product_api.add_url_rule(

    "/products_adm",
    view_func=ProductController_adm.as_view("products_controller_adm"),
    methods = ['POST','GET']
)

#products_adm/id
product_api.add_url_rule(

    "/products_adm/<int:id>",
    view_func=ProductDetails_adm.as_view("product_details_adm"),
    methods = ['GET','PUT','PATCH','DELETE']
)

#products_client
product_api.add_url_rule(

    "/products_client",
    view_func=ProductController_client.as_view("product_controller_client"),
    methods = ['GET']
)

#products_client/id
product_api.add_url_rule(

    "/products_client/<int:id>",
    view_func=ProductDetails_client.as_view("product_details_client"),
    methods = ['GET']
)