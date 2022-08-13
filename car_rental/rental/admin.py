from django.contrib import admin
from rental.models import Department, Car, Customer, Order

admin.site.register(Department)
admin.site.register(Car)
admin.site.register(Customer)
admin.site.register(Order)