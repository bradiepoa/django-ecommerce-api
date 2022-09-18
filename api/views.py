from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view



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

    return Response('Products')
