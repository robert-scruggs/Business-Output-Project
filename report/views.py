from django.shortcuts import render
from django.http import HttpResponse
from .models import SearchLog

# Create your views here.

def say_Hello(request):
    obj = SearchLog(url="www.google.com", iswp=True)
    obj.save()
    return HttpResponse("Hello")



