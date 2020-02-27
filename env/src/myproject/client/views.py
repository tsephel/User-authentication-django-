from django.shortcuts import render
from .models import ClientUpload
from .forms import ClientForm

# Create your views here.
def client_file_view(request):
    client_file = ClientUpload.objects.all()
    contex = {
        'client_file_list': client_file,
    }

    return render(request, 'apps/clientHome.html', contex)

def client_upload_view(request):
    client_form = ClientForm(request.POST or None)
    if client_form.is_valid():
        client_form.save()
    contex = {
        'client_form': client_form,
    }
    return render(request, 'apps/clientUpload.html', contex)

