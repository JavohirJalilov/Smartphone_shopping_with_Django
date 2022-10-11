import json
from urllib import request
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def home(request):
    return JsonResponse({"OK":True})

def add(request):
    data = request.POST.getitem()
    print(data)
    return JsonResponse({'Data':'data'})