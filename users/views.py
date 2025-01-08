from django.shortcuts import render
from django.contrib.auth.models import User
# from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def register(request):
    fname = request.POST.get('firstname')
    lname = request.POST.get('lastname')
    email = request.POST.get('email')
    pass1 = request.POST.get('password')
    pass2 = request.POST.get('password_confirm')
    if request.method == 'POST':
        if pass1 != pass2:
            messages.error(request, 'Parollar bir xil emas')
            return render(request, 'registration/register.html')
        else:
            if User.objects.filter(username=email).exists():
                messages.error(request, f'{email} ushbu emailda foydalanuvchi mavjud !')
                return render(request, 'registration/register.html')
            else:
                user = User.objects.create_user(email, email, pass1)
                user.username = email
                user.first_name = fname
                user.last_name = lname
                user.save()
                # u = authenticate(username=email, password=pass1)
                # messages.success(request, 'Ro‘yxatdan muvaffaqiyatli o‘tingiz !')
                # login(request, u)
                messages.success(request, 'Ro‘yxatdan muvaffaqiyatli o‘tdingiz !')
                return render(request, 'registration/login.html')
    return render(request, 'registration/register.html')