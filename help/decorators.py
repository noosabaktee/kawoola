from django.shortcuts import redirect
from django.http import Http404


def is_login(function):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('abdi')
        else:
            return function(request, *args, **kwargs)
    return wrapper

def is_staff(function):
    def wrapper(request, *args, **kwargs):
        if request.user.is_staff:
            return function(request, *args, **kwargs)
        else:
            raise Http404
    return wrapper