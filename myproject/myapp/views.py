from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework import status
from .models import required_date
#from .serializers import required_serializer
from rest_framework.decorators import api_view

@api_view(('GET',))
def date_view(request):

    return Response(data={},status=status.HTTP_404_NOT_FOUND)



def ping(request):
    json_dict={

    "status":"OK"
    }
    return JsonResponse(json_dict)
