# from django.contrib import admin

# from django.contrib.auth.models import Group
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# from .forms import UserCreationForm
# from .models import MyUser

# # Register your models here.

# class UserAdmin(BaseUserAdmin):
# 	add_form = UserCreationForm

# 	list_display = ('username','email','is_admin')
# 	list_filter = ('username',)

# 	fieldsets = (
# 			(None, {'fields': ('username','email','password')}),
# 			('Permissions', {'fields': ('is_admin',)})
# 		)
# 	search_fields = ('username','email')
# 	ordering = ('username','email')

# 	filter_horizontal = ()


# admin.site.register(MyUser, UserAdmin)


# admin.site.unregister(Group)


# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# from .models import User, user_type


# class UserAdmin(BaseUserAdmin):
#     fieldsets = (
#         (None, {'fields': ('email', 'password', 'name', 'last_login')}),
#         ('Permissions', {'fields': (
#             'is_active',
#             'is_staff',
#             'is_superuser',
#             'groups',
#             'user_permissions',
#         )}),
#     )
#     add_fieldsets = (
#         (
#             None,
#             {
#                 'classes': ('wide',),
#                 'fields': ('email', 'password1', 'password2')
#             }
#         ),
#     )

#     list_display = ('email', 'name', 'is_staff', 'last_login')
#     list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
#     search_fields = ('email',)
#     ordering = ('email',)
#     filter_horizontal = ('groups', 'user_permissions',)


# admin.site.register(User, UserAdmin)

# # We can register our models like before
# # This was the model we commented in the previous snippet.

# admin.site.register(user_type)

#----------------------------------------------------------------

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .forms import UpdateUserForm, AddUserForm

admin.site.site_header = 'Admin Panel'

class UserAdmin(BaseUserAdmin):
    form = UpdateUserForm
    add_form = AddUserForm

    list_display = ('email', 'first_name', 'last_name',)
    list_filter = ('is_active', 'groups' )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'citizen_number')}),
        ('Permissions', {'fields': ('is_active', 'groups')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'email', 'first_name', 'last_name', 'phone_number', 'citizenship_number' 'password1',
                    'password2', 'is_active',
                )
            }
        ),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email', 'first_name', 'last_name')
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
