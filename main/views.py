from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import HttpResponse
from main import services

def preciopromedio(request):
    return HttpResponse(services.get_average_product_price())

def prod_category(request):
    return HttpResponse(services.get_products_filtered_by_category(1))


class ProductAPIView(APIView):
    def get(self, request):
        # TODO
        return Response([])

    def post(self):
        # TODO
        pass
