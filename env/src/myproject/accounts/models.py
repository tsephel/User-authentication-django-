# from django.db import models

# # Create your models here.
# from django.core.validators import RegexValidator

# from django.contrib.auth.models import (
# 		BaseUserManager, AbstractBaseUser
# 	)

# USERNAME_REGEX = '^[a-zA-Z0-9.+-]*$'


# class MyUserManager(BaseUserManager):
#     def create_user(self, username, email, password=None, is_active=True, is_staff=False, is_admin=False):
#         if not email:
#             raise ValueError('Users must have an email address')
#         if not password:
#             raise ValueError('User must have password')
#         user = self.model(username = username,email = self.normalize_email(email))
#         user.set_password(password)
#         user.is_staff = is_staff
#         user.is_admin = is_admin
#         user.is_active = is_active
#         user.save(using=self._db)
#         return user
    
#     def create_staffuser(self,username, email, password=None):
#         user = self.create_user(username, email, password=password, is_staff = True)
#         return user
        
		
#     def create_superuser(self, username, email, password=None):
#         user = self.create_user(username, email, password=password, is_staff=True, is_admin=True)
#         return user



# class MyUser(AbstractBaseUser):
#     username = models.CharField(max_length=300,validators = [RegexValidator(regex = USERNAME_REGEX,message='Username must be alphanumeric or contain numbers',code='invalid_username')],unique=True)
#     email = models.EmailField(max_length=255,unique=True,verbose_name='email address')
#     admin = models.BooleanField(default=False)
#     staff = models.BooleanField(default=False)
#     active = models.BooleanField(default=True)
    
    
#     objects = MyUserManager()
    
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email']
    
#     def __str__(self):
#         return self.email
    
#     def get_short_name(self):
#         return self.email
    
#     def has_perm(self, perm, obj=None):
#         return True
    
#     def has_module_perms(self, app_label):
#         return True
    
#     @property
#     def is_staff(self):
#         "Is the user a member of staff?"
#         return self.staff

#     @property
#     def is_admin(self):
#         "Is the user a admin member?"
#         return self.admin

#     @property
#     def is_active(self):
#         "Is the user active?"
#         return self.active


# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from django.db import models
# from django.utils import timezone


# class UserManager(BaseUserManager):

#     def create_user(self, email, password, is_staff, is_superuser, **extra_fields):
#         if not email:
#             raise ValueError('Users must have an email address')
#         now = timezone.now()
#         email = self.normalize_email(email)
#         user = self.model(
#             email=email,
#             is_staff=is_staff,
#             is_active=True,
#             is_superuser=is_superuser,
#             last_login=now,
#             date_joined=now,
#             **extra_fields
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, email=None, password=None, **extra_fields):
#         return self._create_user(email, password, False, False, **extra_fields)

#     def create_superuser(self, email, password, **extra_fields):
#         user = self._create_user(email, password, True, True, **extra_fields)
#         user.save(using=self._db)
#         return user


# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(max_length=254, unique=True)
#     name = models.CharField(max_length=254, null=True, blank=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     last_login = models.DateTimeField(null=True, blank=True)
#     date_joined = models.DateTimeField(auto_now_add=True)

#     USERNAME_FIELD = 'email'
#     EMAIL_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     objects = UserManager()

#     def get_absolute_url(self):
#         return "/users/%i/" % (self.pk)
#     def get_email(self):
#         return self.email



# class user_type(models.Model):
#     is_teach = models.BooleanField(default=False)
#     is_student = models.BooleanField(default=False)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     def __str__(self):
#         if self.is_student == True:
#             return User.get_email(self.user) + " - is_student"
#         else:
#             return User.get_email(self.user) + " - is_teach"


# ------------------------------------------------------------------

from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(
            self, email, first_name, last_name, citizen_number, password=None,
            commit=True):
        """
        Creates and saves a User with the given email, first name, last name
        and password.
        """
        if not email:
            raise ValueError(_('Users must have an email address'))
        if not first_name:
            raise ValueError(_('Users must have a first name'))
        if not last_name:
            raise ValueError(_('Users must have a last name'))
        if not citizen_number:
            raise ValueError(_('User must have a citizen number'))

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            citizen_number = citizen_number,
        )

        user.set_password(password)
        if commit:
            user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, citizen_number, password):
        """
        Creates and saves a superuser with the given email, first name,
        last name and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            citizen_number=citizen_number,
            commit=False,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name=_('email address'), max_length=255, unique=True
    )
    # password field supplied by AbstractBaseUser
    # last_login field supplied by AbstractBaseUser
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    citizen_number = models.CharField(max_length=40, null=True)

    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'
        ),
    )
    # is_superuser field provided by PermissionsMixin
    # groups field provided by PermissionsMixin
    # user_permissions field provided by PermissionsMixin

    date_joined = models.DateTimeField(
        _('date joined'), default=timezone.now
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'citizen_number']

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def __str__(self):
        return '{} <{}>'.format(self.get_full_name(), self.email)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

