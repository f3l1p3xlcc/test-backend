import pytest
from model_bakery.recipe import Recipe
from main import services
from main import views

generic_product = Recipe(
    "main.Product",
)

generic_category = Recipe(
    "main.Category",
)


@pytest.mark.django_db
def test_get_products_filtered_by_category():
    cat1 = generic_category.make()
    cat2 = generic_category.make()
    prod1 = generic_product.make(price=10, category=cat1)
    prod2 = generic_product.make(price=20, category=cat1)
    generic_product.make(price=30, category=cat2)

    result = services.get_products_filtered_by_category(category_id=cat1.id)

    assert result == [prod1, prod2]


@pytest.mark.django_db
def test_get_average_product_price():
    generic_product.make(price=10)
    generic_product.make(price=20)
    generic_product.make(price=30)
    assert services.get_average_product_price() == 20.0



# TODO rendalo: un test un poco más complejo de python a secas

@pytest.mark.skip
@pytest.mark.django_db
def test_product_list_view(client):
    prod1 = generic_product.make(
        name="prod1",
        price=10,
        stock=2,
        category=generic_category.make(name="cat1"),
    )
    response = client.get("/main/products/")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": prod1.id,
            "name": "prod1",
            "price": 10,
            "stock": 2,
            "category": {
                "id": prod1.category.id,
                "name": "cat1",
            }
        }
    ]


# TODO rendalo: test crear producto



# TODO postulante: test en algo que use todo

@pytest.mark.django_db
def test_preciopromedio(client):
    prod1 = generic_product.make(
        name="prod1",
        price=10,
        stock=2,
        category=generic_category.make(name="cat1"),
    )
    response = client.get("/main/preciopromedio/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_prod_category(client):
    response = client.get("/main/prod_category/?categoria=1")
    assert response.status_code == 200

@pytest.mark.django_db
def test_lista_productos(client):
    prod1 = generic_product.make(
        name="prod1",
        price=10,
        stock=2,
        category=generic_category.make(name="cat1"),
    )
    response = client.get("/main/listadoproductos/")
    assert response.status_code == 200

def test_todo():
    assert 1 == 1






