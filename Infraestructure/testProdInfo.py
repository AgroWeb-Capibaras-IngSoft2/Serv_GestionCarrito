import json
import random

# Abrir y cargar el archivo JSON
def chooseProduct():
    with open("Infraestructure/products.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return random.choice(data["products"])

def getProdInfo(product_id):
    with open("Infraestructure/products.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    for product in data["products"]:
        if product["product_id"] == product_id:
            return product

    return None
