from flask import Blueprint
from .controller import *

cart_api = Blueprint("cart_api",__name__)

#cart_adm/id
cart_api.add_url_rule(

    "/carts_adm/<int:id>",
    view_func=Cart_adm.as_view("cart_adm"),
    methods = ['POST','GET','DELETE']
)

#cart_client/id
cart_api.add_url_rule(

    "/carts_client/<int:id>",
    view_func=Cart_client.as_view("cart_client"),
    methods = ['GET']
)

#add/id/product_id
cart_api.add_url_rule(

    "/add/<int:cart_id>/<int:product_id>",
    view_func=Cart_adding.as_view("add_to_cart"),
    methods = ['PATCH']
)

#buy/id
cart_api.add_url_rule(

    "/buy/<int:id>",
    view_func=Cart_buying.as_view("buy_cart"),
    methods = ['PATCH']
)
