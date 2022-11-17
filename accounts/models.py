from enum import unique
import uuid
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.id = str(uuid.uuid4())[:8]
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.id = str(uuid.uuid4())[:8]
        user.is_staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='メールアドレス',
        max_length=255,
        unique=True,
    )
    id = models.CharField(max_length=25, unique=True, primary_key=True)
    is_staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):             
        return self.email

    def has_perm(self, perm, obj=None):
        return self.admin

    def has_module_perms(self, app_label):
        return self.admin

    @property
    def is_admin(self):
        return self.admin
