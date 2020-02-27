from django.http import HttpResponse
from django.shortcuts import redirect

# @allowed_users(allowed_role = ['watever role we want'])

def allowed_users(allowed_roles=[]) #passing role list
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            #checking if user is part of a group
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name #set group value 
            
            #checking if the group is in allowed role
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You are not authorized to view this page...")
        return wrapper_func
    return decorator