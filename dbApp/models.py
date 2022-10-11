from pyexpat import model
from django.db import models

# Create your models here.

class Smartphone(models.Model):
    name = models.TextField()
    company = models.TextField()
    color = models.TextField()
    RAM = models.TextField()
    memory = models.TextField()
    price = models.TextField()
    img_url = models.TextField()

    def __str__(self):
        return f'Name: {self.name}  Company: {self.company}  RAM: {self.RAM}'