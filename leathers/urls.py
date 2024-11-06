from django.urls import path, re_path
from django.views.decorators.csrf import csrf_exempt
from .views import *


urlpatterns = [
                path('', Index.as_view(), name='index'),
                path('about/', About.as_view(), name='about'),
                path('contacts/', Contacts.as_view(), name='contacts'),
                path('blog/', News_all.as_view(), name='blog'),
                path('conf/', Conf.as_view(), name='conf'),
                path('personal-area/', personal_area, name='personal_area'),
                path('news/<slug:news_slug>/', ShowNews.as_view(), name='news'),
                path("robots.txt", RobotsTxtView.as_view()),
                path("sitemapxml.html", SitemapXmlView.as_view()),
                path("yandex_22b527af66069890.html", YandexView.as_view()),
                
]