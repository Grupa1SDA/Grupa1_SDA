from django.contrib.auth.models import User
from django.db import models

from account.models import Account


class Department(models.Model):
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50, unique=True)
    street = models.CharField(max_length=70)

    def __str__(self):
        return self.city


class Car(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    brand = models.CharField(max_length=50, null=True, blank=True)
    model = models.CharField(max_length=70, null=True, blank=True)
    year = models.CharField(max_length=4, null=True, blank=True)
    fuel = models.CharField(max_length=20, null=True, blank=True)
    seats = models.IntegerField(null=True, blank=True)
    price = models.CharField(max_length=6, null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.model}"


class Customer(models.Model):
    user = models.OneToOneField(Account, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=12, null=True)
    email = models.CharField(max_length=25, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    car_model = models.ForeignKey(Car, null=True, on_delete=models.CASCADE)
    price = models.IntegerField(null=True, blank=False)
    start_rent = models.DateField(auto_now_add=False, null=True)
    end_rent = models.DateField(auto_now_add=False, null=True)
    order_date = models.DateTimeField(auto_now_add=True, null=True)
    pick_up = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    insurance = models.BooleanField(blank=True, null=True, default=False)
    payed = models.BooleanField(null=True, default=False)

    def __str__(self):
        return f"{self.customer} {self.id} "