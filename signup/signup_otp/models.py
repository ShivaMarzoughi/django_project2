from django.db import models

# Create your models here.
# مدل ثبت نام
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=50, verbose_name='fullname')
    phone_number = models.CharField(max_length=15, unique=True, null=False, blank=False, verbose_name='phonenumber')
    otp = models.CharField(max_length=6)
    def __str__(self):
        return self.full_name

