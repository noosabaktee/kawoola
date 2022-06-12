from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.models import User
from abdi.models import Data
from django.shortcuts import redirect
from django.http import HttpResponse, Http404

# Create your views here.

def show_cv(request, username):
    if User.objects.filter(username=username).exists():
        user = User.objects.get(username=username)
        data = Data.objects.get(user=user.username)
        konteks = {
            'user': user,
            'data': data
        }
        return render(request, "template-{}.html".format(data.template), konteks)
    else:
        raise Http404