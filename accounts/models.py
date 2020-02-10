from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Customers(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    profile_pic = models.ImageField(default='bar.png',null=True,blank=True)
    date_create = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return "name:{},email:{},phone:{}".format(self.name, self.email, self.phone)


class Tag(models.Model):
    name = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
        ('indoor', 'indoor'),
        ('outer door', 'outer door'),
    )

    name = models.CharField(max_length=200,null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200,choices=CATEGORY,null=True)
    description = models.TextField(null=True,blank=True)
    date_create = models.DateTimeField(auto_now_add=True,null=True)
    tages = models.ManyToManyField(Tag)

    def __str__(self):
        return "{}--{}".format(self.name,self.tages)



class Order(models.Model):
    # customer =
    # product =

    STATUS = (
              ('pending', 'pending'),
              ('out for delivery','out for delivery'),
              ('delivered', 'delivered')
              )

    customer = models.ForeignKey(Customers, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_create = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.TextField(max_length=10000,null=True)

    def __str__(self):
        return  str(self.customer) + str(self.product) + str(self.STATUS)




