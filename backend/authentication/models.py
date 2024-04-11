import uuid
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager,AbstractBaseUser
from django.utils import timezone
from django.db.models.signals import pre_save

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Create and return a `User` with an email, username and password.
        """
        if not email:
            raise ValueError('Users Must Have an email address')

        user = self.model(
            email=self.normalize_email(
                email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password):
        if password is None:
            return TypeError('Superuser must have password')
        
        user = self.create_user(
            email,password
        )
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user



# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, verbose_name='Public identifier')
    email = models.EmailField(blank=False, unique=True, max_length=255, help_text="Email of User.")
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_vender = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_superuser =  models.BooleanField(default=False)
    is_staff = models.BooleanField(default = False)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

def hash_password(sender, instance, *args, **kwargs):
    if 'pbkdf2_sha256' in instance.password:
        pass
    else:
        instance.set_password(instance.password)
        instance.save()

pre_save.connect(hash_password, sender = User)





 