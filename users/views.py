from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistrationForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('products:index'))
    form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context=context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('products:index'))
    context = {'form': UserRegistrationForm()}
    return render(request, 'users/register.html', context=context)