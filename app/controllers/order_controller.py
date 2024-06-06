from flask import Blueprint, request, jsonify
from ..services import OrderService

order_bp = Blueprint('order', __name__)

@order_bp.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    user_id = data.get('user_id')
    product_id = data.get('product_id')
    quantity = data.get('quantity')
    order = OrderService.create_order(user_id, product_id, quantity)
    return jsonify({"message": "Order created successfully", "order": {"user_id": order.user_id, "product_id": order.product_id, "quantity": order.quantity}}), 201
