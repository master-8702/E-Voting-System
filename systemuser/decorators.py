from django.http import HttpResponse
from django.shortcuts import render, redirect

# this decorator dosn't take any arguments, it will just take the calling function as an argument

def unauthorized_users(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


# this decorator does exactely as the above but it will additinally accept arguments

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None;
            if request.user.group.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You are not authorized to view this page!")
        return wrapper_func
    return decorator


    # or we can check it like this
    # if request.user.groups.filter(name__in=allowed_roles).exists():
    
    #    #This user has (at least) one group that meets authorisation requirement

    #     return view_func(request, *args, **kwargs)

    # else:

    #     #no group found for this user..

    #     return HttpResponse('You are not authorised to view this page')


# this decorator is used when we want to ristrict/allow users based on roles (authorization based on group permission)
def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        
        if group == 'customer':
            return redirect('user-page')
        if group == 'admin':
            return view_func(request, *args **kwargs)

    return wrapper_func


