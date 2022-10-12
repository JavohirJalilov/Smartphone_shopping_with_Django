import json
from unicodedata import name
from urllib import request
from django.shortcuts import render
from django.http import JsonResponse
from .models import Smartphone
# Create your views here.
def home(request):
    return JsonResponse({"OK":True})

def add(request):

    post = request.POST
    name = post.get('name')
    
    company = post.get('company')
    color = post.get('company')
    RAM = post.get('company')
    memory = post.get('company')
    price = post.get('company')
    img_url = post.get('company')
    db = Smartphone(
        name=name, 
        company=company, 
        color=color, RAM=RAM, 
        memory=memory,
        price=price,
        img_url=img_url
        )
    db.save()
    return JsonResponse({'Ok':True})