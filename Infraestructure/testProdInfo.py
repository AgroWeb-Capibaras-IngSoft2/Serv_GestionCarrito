import json
import random

# Abrir y cargar el archivo JSON
def chooseProduct():
    with open("Infraestructure/products.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return random.choice(data["products"])

#
