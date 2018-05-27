from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^home', views.home, name = 'home'),
    url('^$', views.welcome, name = 'welcome'),
    url(r'^search/', views.search_results, name='search_results'),
    url('^accounts/hood_profile/', views.register_hood, name = 'hood_profile'),
    url('^accounts/profile/', views.user_profile, name = 'user_profile'),
    url('^accounts/business_profile/', views.register_business, name = 'register_business'),
    url('^my_profile/', views.my_profile, name = 'my_profile'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)