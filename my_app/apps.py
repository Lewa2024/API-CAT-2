# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory store for products
products = []

# Product Resource Class
class Product:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
    
    def to_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'price': self.price
        }

@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()

    # Validate input
    if not data or 'name' not in data or 'description' not in data or 'price' not in data:
        return jsonify({"error": "Invalid input"}), 400
    
    product = Product(data['name'], data['description'], data['price'])
    products.append(product)

    return jsonify(product.to_dict()), 201

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify([product.to_dict() for product in products]), 200

if __name__ == '__main__':
    app.run(debug=True)




