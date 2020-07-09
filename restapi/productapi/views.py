from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
from rest_framework import status
# Create your views here.

class NotFoundException(Exception):
    pass


class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailView(APIView):
    def get_product(self , pid):
        try:
            product = Product.objects.get(id=pid)
            return product
        except:
            raise NotFoundException()
            
        

    def get(self, request, pid):
        try:
            product = self.get_product(pid)
            serializer = ProductSerializer(product)
            return Response(serializer.data)

        except NotFoundException:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
        
    
    def put(self,request, pid):
        try:
            product = self.get_product(pid)
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except NotFoundException:
            return Response(status=status.HTTP_404_NOT_FOUND)
            

        
    def delete(self, request, pid):
        try:
            product = self.get_product(pid)
            product.delete()
            #return Response(status=status.HTTP_201_OK)
        except NotFoundException:
            return Response(status=status.HTTP_404_NOT_FOUND)
        


