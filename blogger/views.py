from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import LoginForm
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login')

    args = {}
    args.update(csrf(request))
    args['form']  = UserCreationForm()

    return render(request, 'blogger/register.html', args)


def login_user(request):
    print request.method
    form = LoginForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['username']
        print username
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                print 'logged in'
                return HttpResponseRedirect('/home')
        else:
            print 'not loggd in'
            HttpResponseRedirect('/login')
    print 'get request'
    return render(request, 'blogger/login.html', {'form': form})

#
# def logout_user(request):
#         logout(request)
#         return HttpResponseRedirect('/login')


def home(request):
    return render(request, 'blogger/home.html')
