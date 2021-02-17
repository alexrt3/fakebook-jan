from .import bp as api_bp
from flask import jsonify, request
from app.blueprints.shop.models import Product
from app import db

@api_bp.route('/shop', methods=['GET'])
def show_products():
    return jsonify([p.to_dict() for p in Product.query.all()])

@api_bp.route('/shop/create', methods=['POST'])
def create_product():
    data = request.json
    p = Product()
    p.from_dict(data)
    p.save()
    return jsonify(p.to_dict()), 201

@api_bp.route('/shop/delete/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify([p.to_dict() for p in Product.query.all()])