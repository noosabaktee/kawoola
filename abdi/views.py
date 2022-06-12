from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Data

@login_required(login_url=settings.LOGIN_URL)
def profile(request):
    data = Data.objects.get(user=request.user.username)
    konteks = {
        'data': data
    }
    return render(request, "abdi.html", konteks)
    
def customhandler404(request, exception, template_name='404.html'):
    response = render(request, template_name)
    response.status_code = 404
    return response