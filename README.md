<h1 align="center">
  📚 Estudos de E-commerce Unieva
</h1>

* Curso de Engenharia de Software - UniEVANGÉLICA
* Disciplina de Programação Web
* Dev: Thomas NIcholas
* DATA


## :rocket: Sobre o repositório

# Meu App

Esta é uma aplicação back-end em Python usando Flask para gerenciar usuários, produtos e ordens de serviço.

## Tecnologias Utilizadas

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Migrate

## Como Executar

1. **Crie e ative o ambiente virtual**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # ou `venv\Scripts\activate` no Windows
    ```

2. **Instale as dependências**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Inicialize o banco de dados**:
    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

4. **Execute a aplicação**:
    ```bash
    python run.py
    ```

## Rotas Disponíveis

### Usuários

- **Registro**: `POST /api/users/register`
    - **Corpo**: `{ "username": "seu_username", "password": "sua_senha" }`
- **Login**: `POST /api/users/login`
    - **Corpo**: `{ "username": "seu_username", "password": "sua_senha" }`

### Produtos

- **Listar Produtos**: `GET /api/products`
- **Obter Produto por ID**: `GET /api/products/<product_id>`
- **Criar Produto**: `POST /api/products`
    - **Corpo**: `{ "name": "Novo Produto", "price": 30.0 }`

### Ordens

- **Criar Ordem**: `POST /api/orders`
    - **Corpo**: `{ "user_id": 1, "product_id": 2, "quantity": 3 }`

## Testando as Rotas

Use ferramentas como Postman, Insomnia ou CURL para testar as rotas. Exemplos com CURL:

- Registro de Usuário:
    ```bash
    curl -X POST http://localhost:5000/api/users/register -H "Content-Type: application/json" -d '{"username": "seu_username", "password": "sua_senha"}'
    ```

- Login de Usuário:
    ```bash
    curl -X POST http://localhost:5000/api/users/login -H "Content-Type: application/json" -d '{"username": "seu_username", "password": "sua_senha"}'
    ```

- Listar Todos os Produtos:
    ```bash
    curl -X GET http://localhost:5000/api/products
    ```

- Obter Produto por ID:
    ```bash
    curl -X GET http://localhost:5000/api/products/1
    ```

- Criar Novo Produto:
    ```bash
    curl -X POST http://localhost:5000/api/products -H "Content-Type: application/json" -d '{"name": "Novo Produto", "price": 30.0}'
    ```

- Criar Nova Ordem:
    ```bash
    curl -X POST http://localhost:5000/api/orders -H "Content-Type: application/json" -d '{"user_id": 1, "product_id": 2, "quantity": 3}'
    ```
