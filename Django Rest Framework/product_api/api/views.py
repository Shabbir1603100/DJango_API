from django.db.migrations import serializer
from django.shortcuts import render

from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from . import models
from .serializers import AttSerializer
from .models import Att
import requests
from rest_framework import status


# Create your views here.
@api_view(['GET'])
def ShowAll(request):
    atts = Att.objects.all()
    serializer = AttSerializer(atts, many=True)
    return Response(serializer.data)


def _get_time_range(self):
    url = "http://rc.touchtechbd.com/attendance_sync/getTiming/?classesID=2"
    api_request = requests.get(url)

    try:
        api_request.raise_for_status()
        return api_request.json()
    except:
        return None


def save_data(self):
    time_range = self._get_time_range()
    if time_range is not None:
        try:
            url = "http://rc.touchtechbd.com/attendance_sync/Attendance"
            _post_data = requests.post(url, data=models.Att)
            time_range.save()
        except:
            pass


@api_view(['DELETE'])
def deleteAtt(request, pk):
    att = Att.objects.all()
    att.delete()
    return Response('Items delete successfully!')
