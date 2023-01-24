from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from django.shortcuts import render
from django.http import HttpResponse
from main import services
from django.core import serializers


def inicio(request):
    productos = Product.objects.all()

    contexto = {
        'productos':productos
    }

    httpresponse = render(request,'index.html',contexto)
    return httpresponse

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
        productos = Product.objects.all()
        people = serializers.serialize("json", Product.objects.all())
        print(' productos ', productos)
        return Response(people)

    def post(self):
        # TODO
        pass
