from django.contrib import admin
from django.utils.safestring import mark_safe
from django_admin_geomap import ModelAdmin
from .models import *

class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}
    
    
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_photo', 'time_create', 'time_update')
    prepopulated_fields = {"slug": ("title",)}

    def get_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_photo.short_description = 'Фото'
    


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_photo', 'price', 'time_update')
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ('executor',)

    def get_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_photo.short_description = 'Фото'
    
    
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('bayername', 'news')

    def get_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_photo.short_description = 'Фото'


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'lon', 'lat')
    	
    

class Admin(ModelAdmin):
	geomap_default_longitude = "44.6835"
	geomap_default_latitude = "43.0167"
	geomap_default_zoom = "13"
	geomap_field_longitude = 'id_lon'
	geomap_field_latitude = 'id_lat'
	geomap_item_zoom = "18"
	geomap_height = "500px"
	geomap_new_feature_icon = "https://workhub-rso.ru/static/pillow/img/svg7.svg"


class DocumentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'name_pdffile', 'is_published')
    list_display_links = ('id', 'title', 'is_published')
    search_fields = ('title',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}
    

admin.site.register(Location, Admin)
#admin.site.register(Section, SectionAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Products, ProductsAdmin)
#admin.site.register(Review, ReviewAdmin)
admin.site.register(Documents, DocumentsAdmin)
admin.site.site_title = 'Администрирование сайта'
admin.site.site_header = 'Администрирование сайта'
