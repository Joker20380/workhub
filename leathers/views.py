from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.views.generic import ListView, DetailView, TemplateView
from .models import *
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from django_admin_geomap import geomap_context
from .forms import *


class RobotsTxtView(TemplateView):
    template_name = 'robots.txt'
    content_type = 'text/plain'


class YandexView(TemplateView):
    template_name = 'yandex_22b527af66069890.html'


class SitemapXmlView(TemplateView):
    template_name = 'sitemapxml.html'
    content_type = 'application/xml'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = News.objects.filter(is_published=True).order_by('-time_create')
        context['products'] = Products.objects.all()
        context['docs'] = Documents.objects.all()
        return context


class Index(ListView):
    queryset = News.objects.all()
    template_name = "leather/index.html"
    model = News
    paginate_by = 5
    
    
    @staticmethod
    def news_all_index():
        news_all_index = News.objects.all().reverse()
        return news_all_index
        
    @staticmethod
    def products_all_index():
        products_all_index = Products.objects.all().reverse()
        return products_all_index
        
    @staticmethod
    def review_all_index():
        review_all_index = Review.objects.all()
        return review_all_index
        
    
    @staticmethod
    def userprofile_all_index():
        userprofile_all_index = UserProfile.objects.all()
        return userprofile_all_index


class About(ListView):
    queryset = News.objects.all()
    template_name = "leather/about.html"
    model = News
    
    
    @staticmethod
    def news_all_about():
        news_all_about = News.objects.all().reverse()
        return news_all_about
 

    @staticmethod
    def review_all_about():
        review_all_about = Review.objects.all()
        return review_all_about
        
    
    @staticmethod
    def userprofile_all_about():
        userprofile_all_about = UserProfile.objects.all()
        return userprofile_all_about
        
        
class Contacts(ListView):
    queryset = News.objects.all()
    template_name = "leather/contacts.html"
    model = News
    
    
    @staticmethod
    def news_all_contacts():
        news_all_contacts = News.objects.all().reverse()
        return news_all_contacts 
        
        
class News_all(ListView):
    queryset = News.objects.all().reverse()
    template_name = "leather/blog.html"
    model = News
    paginate_by = 5
    
    @staticmethod
    def news_all_news():
        news_all = News.objects.all().reverse()
        return news_all
    
    @staticmethod
    def news_all_review():
    	review_all = Review.objects.all()
    	return review_all
    	
    	
class ShowNews(DetailView):
    model = News
    template_name = 'leather/news-view.html'
    slug_url_kwarg = 'news_slug'
    context_object_name = 'news'
    
    
    @staticmethod
    def news_all_show_news():
        news_all = News.objects.reverse()[:3]
        return news_all
        
    @staticmethod
    def review_all_news_view():
        review_all_news_view = Review.objects.all()
        return review_all_news_view
        
    
    @staticmethod
    def userprofile_all_news_view():
        userprofile_all_news_view = UserProfile.objects.all()
        return userprofile_all_news_view


class Conf(ListView):
    queryset = News.objects.all()
    template_name = "leather/conf.html"
    model = News
    
    
    @staticmethod
    def news_all_conf():
        news_all_conf = News.objects.filter(title= 'Политика конфиденциальности')
        return news_all_conf
        

def personal_area(request):
    if request.method == 'POST':
        form = PersonalAreaForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('personal_area'))
    else:
        form = PersonalAreaForm(instance=request.user)
    context = {'form': form}
    return render(request, 'leather/personal-area.html', geomap_context(Location.objects.filter(id=2), auto_zoom='16', map_height='300px'))
    

	
