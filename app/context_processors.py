from flask import current_app as app
from flask_login import current_user
from app.blueprints.shop.models import Cart, Product

@app.context_processor
def display_cart_info():
    cart_list = {}

    cart = Cart.query.filter_by(user_id=current_user.id).all()
    # print(cart)
    if len(cart) > 0:
        for i in cart:
            p = Product.query.get(i.product_id)
            if i.product_id not in cart_list.keys():
                cart_list[p.id] = {
                    'id': i.id,
                    'product_id': p.id,
                    'quantity': 1,
                    'name': p.name,
                    'description': p.description,
                    'price': p.price,
                    'tax': p.tax
                }
            else:
                cart_list[p.id]['quantity'] += 1
    return {
            'cart': {
                'items': cart,
                'display_cart': cart_list.values()
            } 
         }