from django.db import models
import datetime
# Create your models here.

class Category(models.Model):
  name=models.CharField(max_length=50)

  def __str__(self):         # to appear in the admin module
    return self.name

class Product(models.Model):
  first_name=models.CharField(max_length=20)
  last_name=models.CharField(max_length=20)
  phone=models.CharField(max_length=10)
  email=models.EmailField(max_length=20) 
  password=models.CharField(max_length=15)

  def __str__(self):         # to appear in the admin module
    return f'{self.first_name} + {self.last_name}'

class Customer(models.Model):
  name =models.CharField(max_length=100)
  price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
  category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
  description = models.TextField(max_length=250, default=' ', null=True, blank=True)
  image = models.ImageField(upload_to='uploads/product/')

  def __str__(self):         # to appear in the admin module
    return self.name

class Order(models.Model):
  product=models.ForeignKey(Product, on_delete=models.CASCADE)
  customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
  quantity= models.IntegerField(default=1)
  phone= models.CharField(max_length=20, default='', blank=True)
  date= models.DateField(default=datetime.datetime.today)
  status=models.BooleanField(default=True)

  def __str__(self):         # to appear in the admin module
    return self.product