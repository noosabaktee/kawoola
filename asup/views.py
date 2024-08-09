from django.shortcuts import render
from .forms import RegisterForm, LoginForm
from django.shortcuts import redirect
from abdi.models import Data
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from help.decorators import is_login
# Create your views here.
@is_login
def register(request):
    if request.POST:
        u = request.POST["username"]
        e = request.POST["email"]
        p = request.POST["password1"]
        if not u or not e or not p:
            messages.error(request, 'Form tidak boleh kosong!')
   
        username = u.replace(" ", "").lower()
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username sudah digunakan, silahkan ulangi!')
         
        elif User.objects.filter(email=e).exists():
            messages.error(request, 'Email sudah digunakan, silahkan ulangi!')
        
        elif len(u) < 6 or len(p) < 6:
            messages.error(request, 'Username dan Password min. 5 karakter')
          
        else:
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                user = User.objects.get(username=u)
                color = {
                    'bg-1': '#292b2c',
                    'text-1': '#f7f7f7',
                    'bg-2': '#f7f7f7',
                    'text-2': '#292b2c',
                }
                data = {
                    'user': user.username,
                    'photo': "https://ui-avatars.com/api/?name={}&length=1&%20background=random".format(u),
                    'template': 1,
                    'color': color,
                    'social': {'fb': '', 'ig': '', 'wa': '', 'tw': '', 'in': ''}
                }
                Data.objects.create(**data)
                login(request, user)
                return redirect('abdi')
            
        return redirect('register')
    else:
        konteks = {
            'form': RegisterForm
        }
        return render(request, "register.html", konteks)
        
@is_login
def login_view(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('abdi')
        else:
            messages.error(request, 'Gagal masuk!')
            return redirect('login')
    else:
        konteks = {
            'form': LoginForm
        }
        return render(request, "login.html", konteks)