from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *




class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'last_name', 'first_name', 'patronymic', 'get_image', 'email', 'phone_number', 'address')
    search_fields = ('id', 'username', 'last_name', 'first_name', 'patronymic', 'get_image', 'email', 'phone_number', 'address')
    list_editable = ('email',)
    list_filter = ('username', 'email', 'address')

    def get_image(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50>")

    get_image.short_description = 'Фото'
    

admin.site.register(User, UserAdmin)