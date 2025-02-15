from django.shortcuts import render,redirect
from django.contrib.auth import logout

from django.views.generic import View
# Create your views here.




def my_logout(request):
    logout(request)
    return redirect("/users/login/")


