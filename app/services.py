from .repositories import UserRepository, ProductRepository, OrderRepository

class UserService:# Serviço de Usuários

    @staticmethod
    def register_user(username, password):
        if UserRepository.get_user_by_username(username):
            raise ValueError("Usuário já existe.")
        return UserRepository.create_user(username, password)

    @staticmethod
    def authenticate_user(username, password):
        user = UserRepository.get_user_by_username(username)
        if user and user.check_password(password):
            return user
        return None

class ProductService:# Serviço de Produtos

    @staticmethod
    def get_all_products():
        return ProductRepository.get_all_products()

    @staticmethod
    def get_product_by_id(product_id):
        return ProductRepository.get_product_by_id(product_id)

    @staticmethod
    def create_product(name, price):
        return ProductRepository.create_product(name, price)

class OrderService:# Serviço de Ordens

    @staticmethod
    def create_order(user_id, product_id, quantity):
        return OrderRepository.create_order(user_id, product_id, quantity)
