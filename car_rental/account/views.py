from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from account.forms import RegistrationForm
from account.models import Account

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'account/register.html', context)

def home_screen_view(request):

    context = {}

    accounts = Account.objects.all()
    context['accounts'] = accounts

    return render(request, "account/home.html", context)
