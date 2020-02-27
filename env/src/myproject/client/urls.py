from client import views
from django.urls import path


urlpatterns = [
    path('clienthome/', views.client_file_view, name='client-home'),
    path('clientupload/', views.client_upload_view, name='client-upload'),

]

