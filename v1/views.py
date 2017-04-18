from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class ViewBase(APIView): pass

class IndexView(ViewBase):
  def get(self, request, format=None):
    return Response({'result': 'Hello World!'})
# Create your views here.
