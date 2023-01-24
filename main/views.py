from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from django.shortcuts import render
from django.http import HttpResponse
from main import services

def inicio(request):
    productos = Product.objects.all()

    contexto = {
        'productos':productos
    }
    return render(request,'index.html',contexto)

def preciopromedio(request):
    return HttpResponse(services.get_average_product_price())


def prod_category(request):
    categoria = request.GET['categoria']
    print(categoria)
    productos_cat = []
    productos_cat = services.get_products_filtered_by_category(categoria)
    #return HttpResponse()
    contexto = {
        'productoscat': productos_cat
    }
    return render(request, 'productoscat.html', contexto)


class ProductAPIView(APIView):
    def get(self, request):
        # TODO
        return Response([])

    def post(self):
        # TODO
        pass
