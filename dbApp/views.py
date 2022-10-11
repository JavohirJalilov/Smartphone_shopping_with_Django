import json
from urllib import request
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def home(request):
    return JsonResponse({"OK":True})

def add(request):
    print(request.POST.get('Name'))
    return JsonResponse({"DB":'Added'})