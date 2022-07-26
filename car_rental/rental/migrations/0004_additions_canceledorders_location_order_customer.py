# Generated by Django 4.0.6 on 2022-08-12 15:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rental', '0003_alter_department_city_alter_department_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='Additions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=105)),
                ('insurance', models.IntegerField(blank=True, null=True)),
                ('fuel', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='canceledOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerID', models.CharField(max_length=50, null=True)),
                ('automobileId', models.CharField(max_length=10, null=True)),
                ('price', models.IntegerField(null=True)),
                ('payed', models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickUpPlace', models.CharField(max_length=105, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=70, null=True)),
                ('customerID', models.CharField(max_length=50, null=True)),
                ('carModel', models.CharField(max_length=70, null=True)),
                ('automobileId', models.CharField(max_length=10, null=True)),
                ('price', models.IntegerField(null=True)),
                ('startRent', models.DateField(null=True)),
                ('endRent', models.DateField(null=True)),
                ('orderDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('fullFuel', models.BooleanField(blank=True, default=False, null=True)),
                ('insurance', models.BooleanField(blank=True, default=False, null=True)),
                ('payed', models.BooleanField(default=False, null=True)),
                ('pickUp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rental.location')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('phone', models.CharField(max_length=12, null=True)),
                ('email', models.CharField(max_length=25, null=True)),
                ('dateCreated', models.DateTimeField(auto_now_add=True, null=True)),
                ('profilePic', models.ImageField(blank=True, default='basicUser.jpg', null=True, upload_to='')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
