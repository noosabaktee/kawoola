from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from abdi.models import Data
from django.contrib.auth.models import User
import ast
from django.core.files.storage import FileSystemStorage
from help.func import imgbb
from django.contrib import messages

@login_required(login_url=settings.LOGIN_URL)
def update_social(request):
    if request.POST:
        data = {
            'fb': request.POST['fb'],
            'ig': request.POST['ig'],
            'wa': request.POST['wa'],
            'tw': request.POST['tw'],
            'in': request.POST['in']
        }
        Data.objects.filter(user=request.user.username).update(social=data)
        messages.success(request, 'Data berhasil diubah!')
        
    return redirect('abdi')
    
@login_required(login_url=settings.LOGIN_URL)
def update_color(request):
    if request.POST:
        data = {
            'bg-1': request.POST['bg-1'],
            'text-1': request.POST['text-1'],
            'bg-2': request.POST['bg-2'],
            'text-2': request.POST['text-2']
        }
        Data.objects.filter(user=request.user.username).update(color=data)
        messages.success(request, 'Data berhasil diubah!')
        
    return redirect('abdi')
        
        
@login_required(login_url=settings.LOGIN_URL)
def update_summary(request):
    if request.POST:
        Data.objects.filter(user=request.user.username).update(summary=request.POST['summary'])
        messages.success(request, 'Data berhasil diubah!')
        
    return redirect('abdi')
        
        
@login_required(login_url=settings.LOGIN_URL)
def update_career(request):
    if request.POST:
        Data.objects.filter(user=request.user.username).update(career=request.POST['career'])
        messages.success(request, 'Data berhasil diubah!')
        
    return redirect('abdi')
        
        
@login_required(login_url=settings.LOGIN_URL)
def update_profile(request):
    if request.POST:
        name = request.POST['name']
        address = request.POST['address']
        telp = request.POST['telp']
        website = request.POST['website']
        first, *last = name.split() 
        user = {
            'first_name': first,
            'last_name': " ".join(last)
        }
        data = {
            'website': website,
            'address': address,
            'telp': telp
        }
        User.objects.filter(username=request.user.username).update(**user)
        Data.objects.filter(user=request.user.username).update(**data)
        messages.success(request, 'Data berhasil diubah!')
            
    return redirect('abdi')
        
        
@login_required(login_url=settings.LOGIN_URL)
def update_edu(request):
    if request.POST:
        user = request.user.username
        index = int(request.POST['index'])
        dic = {
            'instansi': request.POST['instansi'],
            'awal': request.POST['awal'],
            'akhir': request.POST['akhir'],
            'jurusan': request.POST['jurusan']
        }
        list = ast.literal_eval(Data.objects.get(user=user).education)
        list[index] = dic
        Data.objects.filter(user=user).update(education=list)
        messages.success(request, 'Data berhasil diubah!')
        
    return redirect('abdi')
    
    
@login_required(login_url=settings.LOGIN_URL)
def update_achievement(request):
    if request.POST:
        user = request.user.username
        index = int(request.POST['index'])
        dic = {
            'prestasi': request.POST['prestasi'],
            'tahun': request.POST['tahun'],
            'tempat': request.POST['tempat']
        }
        list = ast.literal_eval(Data.objects.get(user=user).achievement)
        list[index] = dic
        Data.objects.filter(user=user).update(achievement=list)
        messages.success(request, 'Data berhasil diubah!')
        
    return redirect('abdi')
    
    
@login_required(login_url=settings.LOGIN_URL)
def update_experience(request):
    if request.POST:
        user = request.user.username
        index = int(request.POST['index'])
        dic = {
            'experience': request.POST['experience'],
            'tahun': request.POST['tahun'],
            'tempat': request.POST['tempat'],
            'description': request.POST['description']
        }
        list = ast.literal_eval(Data.objects.get(user=user).experience)
        list[index] = dic
        Data.objects.filter(user=user).update(experience=list)
        messages.success(request, 'Data berhasil diubah!')
        
    return redirect('abdi')
        
        
@login_required(login_url=settings.LOGIN_URL)
def update_template(request):
    if request.POST:
        template = request.POST['template']
        Data.objects.filter(user=request.user.username).update(template=template)
        messages.success(request, 'Data berhasil diubah!')
    
    return redirect('abdi')
        
        
@login_required(login_url=settings.LOGIN_URL)
def update_skill(request):
    if request.POST:
        user = request.user.username
        index = int(request.POST['index'])
        dic = {
            'skill': request.POST['skill'],
            'level': request.POST['level']
        }
        list = ast.literal_eval(Data.objects.get(user=user).skill)
        list[index] = dic
        Data.objects.filter(user=user).update(skill=list)
        messages.success(request, 'Data berhasil diubah!')
        
    return redirect('abdi')
        
        
@login_required(login_url=settings.LOGIN_URL)
def update_photo(request):
    if request.POST:
        u = request.user.username
        f = request.FILES['image']
        fs = FileSystemStorage()       
        file = fs.save(str(f),f)
        url = fs.path(file)
        img = imgbb(url)
        fs.delete(file)
        Data.objects.filter(user=u).update(photo=img)
        messages.success(request, 'Photo berhasil diubah!')
        
    return redirect('abdi')