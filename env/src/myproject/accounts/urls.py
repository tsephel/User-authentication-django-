from accounts import views
from django.urls import path

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
]