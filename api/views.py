from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . models import *
from . serializers import *



# Create your views here.
@api_view(['GET'])    
def getRoutes(request):

    routes = [ 

        {
            'Endpoints':'/notes/',
            'method':'GET',
            'body':None,
            'description':'Returns an array of routes',
        },
        {
            'Endpoints':'/notes/',
            'method':'GET',
            'body':None,
            'description':'Returns an single note object'
        },
    ]

    return Response(routes)

@api_view(['GET'])
def getCategories(request):
    categories = Category.objects.all()
    serializer =  CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getCategory(request,pk):
    categories = Category.objects.get(id=pk)
    serializer =  CategorySerializer(categories, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getProducts(request):

    productlist = Product.objects.all()
    
    serializer =  ProductSerializer(productlist, many=True)

    return Response(serializer.data)

# details page
@api_view(['GET'])
def getProduct(request, pk):

    productlist = Product.objects.get(id=pk)
    
    serializer =  ProductSerializer(productlist, many=False)

    return Response(serializer.data)

