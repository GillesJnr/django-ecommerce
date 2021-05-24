# from django.shortcuts import Http404
from django.http import Http404
from rest_framework.serializers import Serializer
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product, Category
# Create your views here.


class LatestProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:4]
        Serializer = ProductSerializer(products, many=True)
        return Response(Serializer.data) 


class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(Category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404

    
    def get(self,request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)