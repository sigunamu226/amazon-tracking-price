import email
from django.shortcuts import render
from django.http import HttpRequest
from accounts.models import User
from main.common.template_path import accounts_path
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect


# Create your views here.
class AccountView():
    def login(request: HttpRequest):
        success = True
        if request.method == "POST":
            params = request.POST
            user = authenticate(email=params.get('email'), password=params.get('password'))
            if user is not None:
                login(request, user)
                return redirect('items')
            else:
                success = False
        return render(request, accounts_path("login"), {'success': success})

    def signup(request: HttpRequest):
        success = True
        if request.method == "POST":
            params = request.POST
            if User.objects.filter(email = params.get("email")):
                success = False
                return render(request, accounts_path("signup"), {'success': success})
            user = User(email=params.get('email'))
            user.set_password(params.get('password'))
            user.save()
            login(request, user)
            return redirect('items')
        return render(request, accounts_path("signup"), {'success': success})

    def logout(request: HttpRequest):
        logout(request)
        return redirect("login")
