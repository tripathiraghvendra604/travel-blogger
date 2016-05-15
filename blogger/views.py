from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import LoginForm
from .models import Post
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


def home(request):
    return render(request, 'blogger/home.html')

def posts_create(request):
    return HttpResponse('create')


def posts_detail(request):
    return HttpResponse('detail')


def posts_list(request):
    queryset = Post.objects.all()
    context = {
        'title': 'List',
        'object_list': queryset,
    }

    return render(request, 'blogger/list.html', context)


def posts_update(request):
    return HttpResponse('update')


def posts_delete(request):
    return HttpResponse('delete')