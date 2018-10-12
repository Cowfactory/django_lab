from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm, SkillForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        # if post, then authenticate (user submitted username and password)
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print("The account has been disabled.")
                    return HttpResponseRedirect('/')
            else:
                print("The username and/or password is incorrect.")
                return HttpResponseRedirect('/')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

@login_required
def profile(request, username):
    if username == request.user.username:
        user = User.objects.get(username=username)
        # skills = Skill.objects.filter(user=user)
        return render(request, 'profile.html', {'username': username}) #, 'cats': cats})
    else:
        return HttpResponseRedirect('/')

def add_skill(request, username):
    # if username == request.user.username:
    #     form = SkillForm(request.POST)
    #     # validate the form
    #     if form.is_valid():
    #         # don't save the form to the db until it
    #         # has the cat_id assigned

    #     #     new_feeding = form.save(commit=False)
    #     #     new_feeding.cat_id = cat_id
    #     #     new_feeding.save()
    #         return HttpResponseRedirect('/')
    #     # return redirect('cats_detail', cat_id=cat_id)
    # else:
    #     return HttpResponseRedirect('/')
    pass