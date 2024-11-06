from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField



class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    patronymic = models.CharField(max_length=255, null=True, blank=True, verbose_name="Отчество")
    birth = models.DateTimeField(null=True, blank=True, verbose_name="Дата рождения")
    merit = RichTextField(blank=True, verbose_name="Заслуги", null=True)

    def __str__(self):
        if self.patronymic:
            return self.last_name + " " + self.first_name + " " + self.patronymic
        else:
            return self.last_name + " " + self.first_name