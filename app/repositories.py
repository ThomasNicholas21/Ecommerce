from .models import db, User, Product, Order

class UserRepository:# Repositório de Usuários

    @staticmethod
    def get_user_by_username(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def create_user(username, password):
        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return user

class ProductRepository:# Repositório de Produtos

    @staticmethod
    def get_all_products():
        return Product.query.all()

    @staticmethod
    def get_product_by_id(product_id):
        return Product.query.get(product_id)

    @staticmethod
    def create_product(name, price):
        product = Product(name=name, price=price)
        db.session.add(product)
        db.session.commit()
        return product

class OrderRepository: # Repositório de Ordens

    @staticmethod
    def create_order(user_id, product_id, quantity):
        order = Order(user_id=user_id, product_id=product_id, quantity=quantity)
        db.session.add(order)
        db.session.commit()
        return order
