from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import AttSerializer
from .models import Att
import requests
from rest_framework import status

# Create your views here.

"""@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/product-list/',
        'Detail View': '/product-detail/<int:id>/',
        'Create': '/product-create/',
        'Update': '/product-update/<int:id>/',
        'Delete': '/product-detail/<int:id>/',
    }
    return Response(api_urls);
"""

"""@api_view(['GET'])
def ShowAll(request):
    atts = Att.objects.all()
    serializer = AttSerializer(atts, many=True)
    return Response(serializer.data)
"""


@api_view(['GET'])
def ViewAtt(request, classesID=None):
    class_id = request.query_params.get('classId', None)
    if class_id is None:
    #return Bad Request
    result = Att.objects.filter(classesID=class_id)
    # rests are same

    att = Att.objects.filter(classesID)
    serializer = AttSerializer(att, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def CreateAtt(request):

    serializer = AttSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    def deleteAtt(request, pk):
        att = Att.objects.all()
        att.delete()
        return Response('Items delete successfully!')

    return JsonResponse(serializer.errors, status=400)


"""@api_view(['POST'])
def updateAtt(request, pk):
    att = Att.objects.get(id=pk)
    serializer = AttSerializer(instance=att, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
"""
