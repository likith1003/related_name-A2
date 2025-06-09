from django.shortcuts import render
from app.forms import *
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


def login_required(func):
    def inner(request, *args, **kwargs):
        un = request.session.get('username')
        if un:
            return func(request, *args, **kwargs)
        return HttpResponseRedirect(reverse('user_login'))
    return inner


def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST' and request.FILES:
        UFDO = UserForm(request.POST)
        PFDO = ProfileForm(request.POST, request.FILES)
        if UFDO.is_valid() and PFDO.is_valid():
            MUFDO = UFDO.save(commit=False)
            MUFDO.set_password(UFDO.cleaned_data.get('password'))
            MUFDO.save()
            MPFDO = PFDO.save(commit=False)
            MPFDO.user = MUFDO
            MPFDO.save()
            return HttpResponseRedirect(reverse('user_login'))
        return HttpResponse('Invalid data')
    EUFO = UserForm()
    EPFO = ProfileForm()
    return render(request, 'register.html', {'EUFO': EUFO, 'EPFO': EPFO})


def user_login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        AUO = authenticate(username=un, password=pw)
        if AUO:
            login(request, AUO)
            request.session['username'] = un
            return HttpResponseRedirect(reverse('home'))
        messages.error(request, 'Invalid Credentials')
        return HttpResponseRedirect(reverse(user_login))
    return render(request, 'user_login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def create_todo(request):
    if request.method == 'POST':
        un = request.session.get('username')
        UO = User.objects.get(username=un)
        TFDO = TodoForm(request.POST)
        if TFDO.is_valid():
            MTFDO = TFDO.save(commit=False)
            MTFDO.user=UO
            MTFDO.save()
            messages.info(request, 'Todo Created Successfully')
            return HttpResponseRedirect(reverse('create_todo'))
        return HttpResponse('invalid Data')
    ETFO = TodoForm()
    return render(request, 'create_todo.html', {'ETFO':ETFO})


@login_required
def my_list(request):
    # un = request.session.get('username')
    # UO = User.objects.get(username=un)
    # all_todos = Todo.objects.filter(user=UO)
    # return render(request, 'my_list.html', {'all_todos': all_todos})
    #---------------------or-----------------
    return render(request, 'my_list.html')