# Create your models here.
from django.db import models

class CarBody(models.Model):
    # class Car(models.TextChoices):
    car_choices = (
        ("Sedan", "Sedan"),
        ("Hatchback", "Hatchback"),
        ("Kombi", "Kombi"),
        ("SUV", "SUV"),
        ("Roadster", "Roadster"),
        ("Liftback", "Liftback"),
        ("Crossover", "Crossover"),
        ("Kabriolet", "Kabriolet"),
        ("Pick-up", "Pick-up"),
        ("Coupe", "Coupe"),
        ("VAN", "VAN"),
        ("Minivan", "Minivan"),

    )

    car_body = models.CharField(max_length=20,
                            choices = car_choices,
                            default = "Sedan")

    #year = models.ForeignKey(Year, on_delete=models.CASCADE, null=True)
    about = models.TextField(max_length=355, null=True, blank=True)
    shortAbout = models.CharField(max_length=70, null=True, blank=True)
    mark = models.CharField(max_length=50, null=True, blank=True)
    model = models.CharField(max_length=70, null=True, blank=True)
    engine_size = models.CharField(max_length=9, null=True, blank=True)
    mass = models.CharField(max_length=10, null=True, blank=True)
    production_year = models.CharField(max_length=4, null=True, blank=True)
    v_max = models.IntegerField(null=True, blank=True)
    horse_power = models.IntegerField(null=True, blank=True)
    seats = models.IntegerField(null=True, blank=True)
    airbags = models.CharField(max_length=2, null=True, blank=True)
    doors = models.IntegerField(null=True, blank=True)
    price = models.FloatField(max_length=10, null=True, blank=True)
    insurance = models.IntegerField(null=True, blank=True)
    fuel = models.IntegerField(null=True, blank=True)
    fuel_tank = models.IntegerField(null=True, blank=True)
    avg_fuel_consumption = models.IntegerField(null=True, blank=True)
    gearbox = models.IntegerField(null=True, blank=True)
    drive = models.IntegerField(null=True, blank=True)
    colour = models.IntegerField(null=True, blank=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.model