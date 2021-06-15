from django.http import HttpResponse
from django.shortcuts import redirect

def unauth_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect("/inside/inside1")
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func

def allowed_user(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            grp=None
            if request.user.groups.exists():
                grp=request.user.groups.all()[0].name
            if grp in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorised to view this page')
        return wrapper_func
    return decorator