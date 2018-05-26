from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^home', views.home, name = 'home'),
    url('^$', views.welcome, name = 'welcome'),
    url(r'^search/', views.search_results, name='search_results'),
    url('^accounts/profile/', views.user_profile, name = 'user_profile'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)