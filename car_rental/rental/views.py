from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count, Max
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from rental.models import Car, Order


def car_screen_view(request):

    context = {}

    cars = Car.objects.all()
    context['cars'] = cars

    return render(request, "cars.html", context)

def car_detail(request, id=None):

    context = {}

    detail = get_object_or_404(Car, id=id)
    context = {
        "detail": detail
    }
    return render(request, 'car_detail.html', context)


def order_created(request):
    form = Order(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "form": form,
        "title": "Create Order"
    }
    return render(request, 'order_create.html', context)

