from email.policy import default
import os
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from APA_module.apa_validations import is_valid_iran_code, validate_image


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    return os.path.join(f'user/{instance.id}/profile_image/', filename)

def get_default_profile_image():
	return "logos/user.png"


class User(AbstractUser):
    email               = models.EmailField(verbose_name='ایمیل', unique=True)
    national_code       = models.CharField(verbose_name='کد ملی',validators=[is_valid_iran_code], null=True, max_length=10)
    mobile_number1      = models.CharField(verbose_name='شماره همراه', max_length=11, null=True,blank = True, unique=True)
    mobile_number2      = models.CharField(verbose_name='شماره همراه', max_length=11, null=True,blank = True, unique=True)
    birthdate           = models.IntegerField(verbose_name='سال تولد', blank=True, null=True)
    address             = models.CharField(verbose_name='آدرس', max_length=200, blank=True, default='اهواز')
    profile_picture     = models.ImageField(verbose_name='عکس پروفایل', validators=[validate_image], upload_to=get_file_path, default=get_default_profile_image, null=True, blank=True)

    def __str__(self):
        return str(self.id)

