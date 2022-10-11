from django.urls import path
from .views import home, add

urlpatterns = [
    path('', home, name='home page'),
    path('add/', add, name='Add database field')
]
