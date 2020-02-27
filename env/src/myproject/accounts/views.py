# from django.shortcuts import render, redirect
# from django.contrib.auth import login, get_user_model, logout

# from django.http import HttpResponseRedirect
# # Create your views here.
# from .forms import UserCreationForm, UserLoginForm

# def home_view(request):
#     return render(request, 'apps/home.html', {})

# def register(request, *args, **kwargs):
# 	form = UserCreationForm(request.POST or None)
# 	if form.is_valid():
# 		form.save()
# 		return redirect('login')
# 	context = {
# 		'form': form
# 	}
# 	return render(request, "apps/register.html", context)


# def login_view(request, *args, **kwargs):
#     form = UserLoginForm(request.POST or None)
#     if form.is_valid():
#         user_obj = form.cleaned_data.get('user_obj')
#         login(request, user_obj)
#         return redirect('home')
#     return render(request, "apps/login.html", {"form": form})


# def logout_view(request):
#     logout(request)
#     return redirect('login')


# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
# from .models import user_type, User

# def shome_view(request):
#     if request.user.is_authenticated and user_type.objects.get(user=request.user).is_student:
#         return render(request,'apps/shome.html')
#     elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_teach:
#         return redirect('thome')
#     else:
#         return redirect('login')
                      
# def thome_view(request):
#     if request.user.is_authenticated and user_type.objects.get(user=request.user).is_teach:
#         return render(request,'apps/thome.html')
#     elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_student:
#         return redirect('shome')
#     else:
#         return redirect('home')

# def register_view(request):
#     if (request.method == 'POST'):
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         st = request.POST.get('student')
#         te = request.POST.get('teacher')
        
#         user = User.objects.create_user(
#             email=email,
#         )
#         user.set_password(password)
#         user.save()
        
#         usert = None
#         if st:
#             usert = user_type(user=user,is_student=True)
#         elif te:
#             usert = user_type(user=user,is_teach=True)
        
#         usert.save()
#         #Successfully registered. Redirect to homepage
#         return redirect('home')
#     return render(request, 'apps/register.html', {'user': user})
    
# def login_view(request):
#     if (request.method == 'POST'):
#         email = request.POST.get('email') #Get email value from form
#         password = request.POST.get('password') #Get password value from form
#         user = authenticate(request, email=email, password=password)
        
#         if user is not None:
#             login(request, user)
#             type_obj = user_type.objects.get(user=user)
#             if user.is_authenticated and type_obj.is_student:
#                 return redirect('shome') #Go to student home
#             elif user.is_authenticated and type_obj.is_teach:
#                 return redirect('thome') #Go to teacher home
#         else:
#             # Invalid email or password. Handle as you wish
#             return redirect('home')

#     return render(request, 'apps/login.html', {'user': user})

#--------------------------------------------------------------------

from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model, logout, authenticate
from .forms import AddUserForm, LoginForm
from django.contrib.auth.models import Group
from django.http import HttpResponse

def home_view(request):
    return render(request, 'apps/home.html', {})

def register_view(request):
    register_form = AddUserForm(request.POST or None)
    if register_form.is_valid():
        user = register_form.save(commit=False)
        user = register_form.save()
        # group = Group.objects.get(name='group')
        # group.user_set.add(user)
        # request.user.groups.add('group')
        raw_password = register_form.cleaned_data.get('password1')

        user = authenticate(request, email=user.email, password=raw_password)
        if user is not None:
            login(request, user)
        else:
            print("user is not authenticated")
        return redirect('login')
    
    return render(request, 'apps/register.html', {'register_form': register_form})

def login_view(request):
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None and user.is_active:
            login(request, user)
        else:
            return HttpResponse('Your account is not activated. Please contact this number or send a mail for verification.')
        return redirect('home')
        
    return render(request, 'apps/login.html', {'login_form': login_form})

def logout(request):
    logout(request)
    return redirect('login')
