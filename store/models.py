from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer( models.Model ):
    user=models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=200, null=True)
    email=models.EmailField(max_length=200)
    def __str__(self):
        return self.name


class Product( models.Model ):
    name=models.CharField(max_length=200)
    price=models.FloatField()
    digital=models.BooleanField(default=False, null=True, blank=True)
    image=models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url

class Order( models.Model ):
    customer=models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_order=models.DateTimeField(default=False)
    transition_id = models.CharField(max_length=100, null=True)

    def __str__ (self):
        return str(self.id)

    @property
    def shipping(self):
        shipping=False
