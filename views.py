from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from .models import Furniture
from .serializers import FurnitureSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def furniture_list(request):
    """
    List all furniture.
    """
    if request.method == 'GET':
        furniture = Furniture.objects.all()
        serializer = FurnitureSerializer(furniture, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def furniture_detail(request, pk):
    """
    Retrieve a furniture instance.
    """
    try:
        furniture = Furniture.objects.get(pk=pk)
    except Furniture.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = FurnitureSerializer(furniture)
        return Response(serializer.data)
