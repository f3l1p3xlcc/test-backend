from django import urls
from django.urls import include, path

from main import views
from main.views import preciopromedio
from main.views import prod_category

urlpatterns = [
    path("products/", views.ProductAPIView.as_view()),
    path("preciopromedio/", preciopromedio),
    path("prod_category/", prod_category),
]

"""
urlpatterns = [
    path("products/", include("domains.rest.suppliers.v100.urls")),
]
"""
