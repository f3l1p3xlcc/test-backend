from model_bakery.recipe import Recipe

generic_product = Recipe(
    "main.Product",
)

generic_category = Recipe(
    "main.Category",
)

def get_average_product_price() -> float:
    cat1 = generic_category.make()
    cat2 = generic_category.make()
    prod1 = generic_product.make(price=10, category=cat1, name='nombre')
    prod2 = generic_product.make(price=20, category=cat1)
    return (prod2.get_price() + prod1.get_price()) /2



def get_products_filtered_by_category(category_id: int) -> list:
    cat1 = generic_category.make(id=1)
    cat2 = generic_category.make(id=2)
    prod1 = generic_product.make(price=10, category=cat1, name='nombre')
    prod2 = generic_product.make(price=20, category=cat2)
    prodcat = prod2.get_category()
    return prodcat.get_id()



