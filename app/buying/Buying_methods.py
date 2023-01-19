from app.carts.models import my_carts as carts
from app.products.models import my_products as products

def add_to_cart(client_id,product_id):

    for cart in carts:
        if cart['id'] == client_id:
            
            for product in products:
                if product['id'] == product_id:
                    
                    if product['quantidade'] == 0: return {}, 400 
                    
                    else:
                        cart['produtos'] = cart['produtos'].append(product)
                        return{}, 200
    return{}, 404

def buy_cart(client_id):

    for cart in carts:
        if cart['id'] == client_id:
            
            for product in cart['produtos']:
                
                if product['quantidade'] == 0: return {}, 400

                else:
                    product['quantidade'] -= 1

            return{'Parabéns pela compra'}, 200