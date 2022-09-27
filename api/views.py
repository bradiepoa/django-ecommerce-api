from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . models import Product
from . serializers import ProductSerializer



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

