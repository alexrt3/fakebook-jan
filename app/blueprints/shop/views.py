from .import bp as shop_bp
from flask import render_template

@shop_bp.route('/')
def home():
    context = {}
    return render_template('shop/home.html', **context)