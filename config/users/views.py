from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserRegisterForm
from .models import Profile
# Create your views here.


def register(request):
    form = CustomUserRegisterForm()
    if request.method == "POST":
        form = CustomUserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user) # yangi profil ochish va uni userga biriktirish
            login(request,user) # auth usermi login qilish
            return redirect("/")
        else:
            print("Error")
            return render(request, "auth/register.html")
    return render(request, "auth/register.html", context={"form":form})