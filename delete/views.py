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
def del_edu(request):
    if request.POST:
        user = request.user.username
        index = int(request.POST['index'])
        list = ast.literal_eval(Data.objects.get(user=user).education)
        del list[index]
        if(len(list) > 0):
            Data.objects.filter(user=user).update(education=list)
        else:
            Data.objects.filter(user=user).update(education="")

        messages.error(request, 'Data berhasil dihapus!')
        
    return redirect('abdi')
    
    
@login_required(login_url=settings.LOGIN_URL)
def del_achievement(request):
    if request.POST:
        user = request.user.username
        index = int(request.POST['index'])
        list = ast.literal_eval(Data.objects.get(user=user).achievement)
        del list[index]
        if(len(list) > 0):
            Data.objects.filter(user=user).update(achievement=list)
        else:
            Data.objects.filter(user=user).update(achievement="")

        messages.error(request, 'Data berhasil dihapus!')
        
    return redirect('abdi')
    
    
@login_required(login_url=settings.LOGIN_URL)
def del_experience(request):
    if request.POST:
        user = request.user.username
        index = int(request.POST['index'])
        list = ast.literal_eval(Data.objects.get(user=user).experience)
        del list[index]
        if(len(list) > 0):
            Data.objects.filter(user=user).update(experience=list)
        else:
            Data.objects.filter(user=user).update(experience="")

        messages.error(request, 'Data berhasil dihapus!')
        
    return redirect('abdi')
    
    
@login_required(login_url=settings.LOGIN_URL)
def del_skill(request):
    if request.POST:
        user = request.user.username
        index = int(request.POST['index'])
        list = ast.literal_eval(Data.objects.get(user=user).skill)
        del list[index]
        if(len(list) > 0):
            Data.objects.filter(user=user).update(skill=list)
        else:
            Data.objects.filter(user=user).update(skill="")

        messages.error(request, 'Data berhasil dihapus!')
        
    return redirect('abdi')
    