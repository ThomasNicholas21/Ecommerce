from flask import Blueprint, request, jsonify
from ..services import UserService

user_bp = Blueprint('user', __name__) # Cria um blueprint para os endpoints de usuários


@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    try:
        user = UserService.register_user(username, password)
        return jsonify({"message": "User registered successfully", "user": user.username}), 201
    except ValueError as e:
        return jsonify({"message": str(e)}), 400

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = UserService.authenticate_user(username, password)
    if user:
        return jsonify({"message": "Login successful", "user": user.username}), 200
    return jsonify({"message": "Invalid credentials"}), 401
