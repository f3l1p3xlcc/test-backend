from model_bakery.recipe import Recipe
from .models import Product
from statistics import mean

generic_product = Recipe(
    "main.Product",
)

generic_category = Recipe(
    "main.Category",
)

def get_average_product_price() -> float:
    promedio = 0.0
    productos = Product.objects.all()
    elementos = []
    for i in productos:
        elementos.append(i.price)
    promedio = mean(elementos)
    return promedio



def get_products_filtered_by_category(category_id: int) -> list:
    print('category_id',category_id)
    productos = Product.objects.filter(category_id=category_id)
    print(productos)
    return productos



