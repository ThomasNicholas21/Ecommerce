from flask import Blueprint, request, jsonify
from ..services import ProductService

product_bp = Blueprint('product', __name__) # Cria um blueprint para os endpoints de produtos


@product_bp.route('/products', methods=['GET'])
def get_all_products():
    products = ProductService.get_all_products()
    return jsonify([product.name for product in products]), 200

@product_bp.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = ProductService.get_product_by_id(product_id)
    if product:
        return jsonify({"name": product.name, "price": product.price}), 200
    return jsonify({"message": "Product not found"}), 404

@product_bp.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    name = data.get('name')
    price = data.get('price')
    product = ProductService.create_product(name, price)
    return jsonify({"message": "Product created successfully", "product": {"name": product.name, "price": product.price}}), 201
