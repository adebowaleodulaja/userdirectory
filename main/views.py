from django.shortcuts import render, redirect
#from django.http import HttpResponse, HttpResponseRedirect

from .models import User
from .forms import UserForm


def home(request):
    return render(request, "main/home.html")


def create_user(request):
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_user')
    else:
        form = UserForm()
    return render(request, "main/create_user.html", {'form': form})


def list_user(request):
    userList = User.objects.all()
    print(userList)
    return render(request, "main/list_user.html", {'userList': userList})
