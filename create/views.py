from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from abdi.models import Data
from django.contrib.auth.models import User
import ast
from django.contrib import messages

# Create your views here.
@login_required(login_url=settings.LOGIN_URL)
def add_edu(request):
    if request.POST:
        user = request.user.username
        dic = {
            'instansi': request.POST['instansi'],
            'awal': request.POST['awal'],
            'akhir': request.POST['akhir'],
            'jurusan': request.POST['jurusan']
        }
        list = Data.objects.get(user=user).education
        list = [] if not list else ast.literal_eval(list)
        list.append(dic)
        Data.objects.filter(user=user).update(education=list)
        messages.success(request, 'Data berhasil ditambahkan!')
        
    return redirect('abdi')
    
    
@login_required(login_url=settings.LOGIN_URL)
def add_achievement(request):
    if request.POST:
        user = request.user.username
        dic = {
            'prestasi': request.POST['prestasi'],
            'tahun': request.POST['tahun'],
            'tempat': request.POST['tempat']
        }
        list = Data.objects.get(user=user).achievement
        list = [] if not list else ast.literal_eval(list)
        list.append(dic)
        Data.objects.filter(user=user).update(achievement=list)
        messages.success(request, 'Data berhasil ditambahkan!')
        
    return redirect('abdi')
    
    
@login_required(login_url=settings.LOGIN_URL)
def add_experience(request):
    if request.POST:
        user = request.user.username
        dic = {
            'experience': request.POST['experience'],
            'tahun': request.POST['tahun'],
            'tempat': request.POST['tempat'],
            'description': request.POST['description']
        }
        list = Data.objects.get(user=user).experience
        list = [] if not list else ast.literal_eval(list)
        list.append(dic)
        Data.objects.filter(user=user).update(experience=list)
        messages.success(request, 'Data berhasil ditambahkan!')
        
    return redirect('abdi')
        
   
@login_required(login_url=settings.LOGIN_URL)
def add_skill(request):
    if request.POST:
        user = request.user.username
        dic = {
            'skill': request.POST['skill'],
            'level': request.POST['level']
        }
        list = Data.objects.get(user=user).skill
        list = [] if not list else ast.literal_eval(list)
        list.append(dic)
        Data.objects.filter(user=user).update(skill=list)
        messages.success(request, 'Data berhasil ditambahkan!')
        
    return redirect('abdi')