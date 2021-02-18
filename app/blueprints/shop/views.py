from .import bp as shop_bp
from flask import render_template, redirect, url_for, flash, request
from app.blueprints.shop.models import Product, Cart
from flask_login import current_user
from app import db

@shop_bp.route('/')
def home():
    context = {
        'products': Product.query.all()
    }
    return render_template('shop/home.html', **context)

@shop_bp.route('/product/add')
def add_product():
    try:
        _id = request.args.get('id')
        p = Product.query.get(_id)
        c = Cart(user_id=current_user.id, product_id=p.id)
        c.save()
        flash(f'{p.name} was added successfully', 'success')
    except Exception as error:
        print(error)
        flash(f'{p.name} was not added successfully. Try again.', 'danger')
    return redirect(url_for('shop.home'))

@shop_bp.route('/cart')
def cart():
    context = {}
    return render_template('shop/cart.html', **context)

@shop_bp.route('/cart/delete')
def delete_product():
    p = Product.query.get(request.args.get('product_id'))
    cart = current_user.cart
    for i in cart:
        if i.product_id == p.id and current_user.id == i.user_id:
            cart_item = Cart.query.filter_by(user_id=current_user.id).first()
            db.session.delete(cart_item)
    db.session.commit()
    flash(f'Product deleted', 'info')
    return redirect(url_for('shop.cart'))

@shop_bp.route('/checkout')
def checkout():
    context = {}
    return render_template('shop/checkout.html', **context)