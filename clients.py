# client.py
import requests
import json

# API endpoint
api_url = "http://127.0.0.1:5000/products"

# Add new products
def add_product(name, description, price):
    product = {
        "name": name,
        "description": description,
        "price": price
    }
    response = requests.post(api_url, json=product)
    if response.status_code == 201:
        print(f"Product created: {response.json()}")
    else:
        print("Failed to create product:", response.json())

# Get all products
def get_products():
    response = requests.get(api_url)
    if response.status_code == 200:
        products = response.json()
        print("Products List:")
        for product in products:
            print(f"Name: {product['name']}, Price: {product['price']}")
    else:
        print("Failed to retrieve products")

# Add some products
add_product("Laptop", "A high-end laptop", 1200.50)
add_product("Smartphone", "Latest model smartphone", 799.99)

# Retrieve and display products
get_products()

#POST/products
#requestbody(JSON)
data = {
    "name": "Product Name",
    "description": "Product Description",
    "price": 100.50
}
#respone (JSON)
{
  "name": "Product Name",
  "description": "Product Description",
  "price": 100.50
}
# GET/products
# response(JSON)
[
  {
    "name": "Product 1",
    "description": "Description 1",
    "price": 20.50
  },
  {
    "name": "Product 2",
    "description": "Description 2",
    "price": 30.00
  }
]

#Error handling
{"error": "Invalid input"}





