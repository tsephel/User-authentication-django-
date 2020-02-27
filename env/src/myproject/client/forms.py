from django import forms
from .models import ClientUpload

class ClientForm(forms.ModelForm):
    class Meta:
        model = ClientUpload
        fields = ('client_upload', 'deadline', 'price')