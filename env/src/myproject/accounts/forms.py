# # accounts.forms.py
# from django.contrib.auth import get_user_model
# from django.db.models import Q

# from django import forms

# User = get_user_model()

# class UserCreationForm(forms.ModelForm):
# 	password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
# 	password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

# 	class Meta:
# 		model = User
# 		fields = ['username', 'email']

# 	def clean_password(self):
# 		password1 = self.cleaned_data.get('password1')
# 		password2 = self.cleaned_data.get('password2')
# 		if password1 and password2 and password1 != password2:
# 			raise forms.ValidationError("Passwords do not match")
# 		return password2

# 	def save(self, commit=True):
# 		user = super(UserCreationForm, self).save(commit=False)
# 		user.set_password(self.cleaned_data['password1'])

# 		if commit:
# 			user.save()
# 		return user


# class UserLoginForm(forms.Form):
# 	query = forms.CharField(label='Username / Email')
# 	password = forms.CharField(label='Password', widget=forms.PasswordInput)

# 	def clean(self, *args, **kwargs):
# 		query = self.cleaned_data.get('query')
# 		password = self.cleaned_data.get('password')
# 		user_qs_final = User.objects.filter(
# 				Q(username__iexact=query) |
# 				Q(email__iexact=query)
# 			).distinct()
# 		if not user_qs_final.exists() and user_qs_final.count != 1:
# 			raise forms.ValidationError("Invalid credentials - user does note exist")
# 		user_obj = user_qs_final.first()
# 		if not user_obj.check_password(password):
# 			raise forms.ValidationError("credentials are not correct")
# 		self.cleaned_data["user_obj"] = user_obj
# 		return super(UserLoginForm, self).clean(*args, **kwargs)

#--------------------------------------------------------------------

from django import forms
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import Group

class AddUserForm(forms.ModelForm):
    """
    New User Form. Requires password confirmation.
    """
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Confirm password', widget=forms.PasswordInput
    )

    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True)

    # CHOICES= (('Client', 'Client'),('Professional', 'Professional'),)
    # Label = forms.ChoiceField(choices=CHOICES, label='Label', widget=forms.RadioSelect())

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'citizen_number', 'group')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = False
        if commit:
            user.save()
            user.groups.add(self.cleaned_data['group'])
        return user


class UpdateUserForm(forms.ModelForm):
    """
    Update User Form. Doesn't allow changing password in the Admin.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = (
            'email', 'password', 'first_name', 'last_name', 'is_active',
        )

    def clean_password(self):
# Password can't be changed in the admin
        return self.initial["password"]

class LoginForm(forms.Form): # Note: forms.Form NOT forms.ModelForm
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control','type':'text','name': 'email','placeholder':'Email'}), 
        label='Email')
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control','type':'password', 'name': 'password','placeholder':'Password'}),
        label='Password')

    class Meta:
        fields = ['email', 'password']