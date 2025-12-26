from django.urls import path, re_path
from django.views.decorators.csrf import csrf_exempt
from .views import *


urlpatterns = [
                path('', Index.as_view(), name='index'),
                path('med/', Index_med.as_view(), name='index_med'),
                path('mediplus/', Index_mediplus.as_view(), name='index_mediplus'),
                path('medicare/', Index_medicare.as_view(), name='index_medicare'),
                path('about/', About.as_view(), name='about'),
                path('contacts/', Contacts.as_view(), name='contacts'),
                path('blog/', News_all.as_view(), name='blog'),
                path('conf/', Conf.as_view(), name='conf'),
                path('personal-area/', personal_area, name='personal_area'),
                path('news/<slug:news_slug>/', ShowNews.as_view(), name='news'),
                path('products/<slug:products_slug>/', ShowProducts.as_view(), name='products'),
                path('product/<int:products_id>/add_user/', add_user_to_product, name='add_user_to_product'),
                path("robots.txt", RobotsTxtView.as_view()),
                path("sitemapxml.html", SitemapXmlView.as_view()),
                path("yandex_22b527af66069890.html", YandexView.as_view()),
                
]