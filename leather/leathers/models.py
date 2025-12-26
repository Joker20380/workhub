from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.conf import settings
from django_admin_geomap import GeoItem
from users.models import *


class Section(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название раздела", db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
	
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('section', kwargs={'section_slug': self.slug})

    class Meta:
        verbose_name = 'Раздел сайта'
        verbose_name_plural = 'Разделы сайта'
        ordering = ['id']



class Location(models.Model, GeoItem):
	name = models.CharField(max_length=100)
	lon = models.FloatField(null=True, blank=True)
	lat = models.FloatField(null=True, blank=True)
	
	def __str__(self):
		return self.name
	
	@property
	def geomap_longitude(self):
		return '' if self.lon is None else str(self.lon)
		
	@property
	def geomap_latitude(self):
		return '' if self.lat is None else str(self.lat)

	@property
	def geomap_popup_view(self):
		return str(self)
		
	@property
	def geomap_popup_edit(self):
		return self.geomap_popup_view
		
	@property
	def geomap_popup_common(self):
		return self.geomap_popup_view
		
	@property
	def geomap_icon(self):
		return self.default_icon

    	

class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = RichTextField(blank=True, verbose_name="Текст")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото", blank=True, null=True)
    time_create = models.DateTimeField(verbose_name="Дата и время создания")
    time_update = models.DateTimeField(verbose_name="Дата и время обновления")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
	
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news', kwargs={'news_slug': self.slug})
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        unique_together = [['title', 'slug']]
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        
        
class Review(models.Model):
    news = models.ForeignKey(News, on_delete=models.PROTECT, related_name='review', verbose_name='Название новости', blank=True, null=True)
    buyer = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user', verbose_name='Покупатель', blank=True, null=True)
    body = RichTextField(verbose_name='Отзыв')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False, verbose_name='Опубликовать')

    class Meta:
        ordering = ('created',)
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return 'Отзыв от {} на {}'.format(self.bayername, self.news)


class Documents(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = RichTextField(blank=True, verbose_name="Содержание")
    name_pdffile = models.CharField(max_length=255, verbose_name="Имя PDF файла", null=True, blank=True)
    pdffile = models.FileField(upload_to="pdf/%Y/%m/%d/", verbose_name="PDF", null=True, blank=True)
    time_create = models.DateTimeField(verbose_name="Время создания")
    time_update = models.DateTimeField(verbose_name="Дата публикации")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
	
    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('docs', kwargs={'docs_slug': self.slug})
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
        ordering = ['time_create']        
        
        
class Products(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = RichTextField(blank=True, verbose_name="Текст")
    price = models.DecimalField(decimal_places=2, max_digits=20, default=0.00, verbose_name="Цена")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото", blank=True, null=True)
    photo2 = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото2", blank=True, null=True)
    photo3 = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото3", blank=True, null=True)
    photo4 = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото4", blank=True, null=True)
    photo5 = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото5", blank=True, null=True)
    photo6 = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото6", blank=True, null=True)
    time_create = models.DateTimeField(verbose_name="Дата и время создания")
    time_update = models.DateTimeField(verbose_name="Дата и время обновления")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    number_of_employees = models.IntegerField(verbose_name="Количество сотрудников", max_length=2, default=0)
    location = models.ManyToManyField(Location, related_name="products", verbose_name="Местоположение", blank=True, null=True)
    executor = models.ManyToManyField(User, related_name='products', verbose_name='Исполнитель', blank=True, null=True)

	
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('products', kwargs={'products_slug': self.slug})
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


    class Meta:
        unique_together = [['title', 'slug']]
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'        
        
        
        
        