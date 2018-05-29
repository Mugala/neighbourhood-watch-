from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^home', views.home, name='home'),
    url(r'^$', views.welcome, name='welcome'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^accounts/hood_profile/', views.register_hood, name='hood_profile'),
    url(r'^accounts/profile/', views.user_profile, name='user_profile'),
    url(r'^accounts/business_profile/',
        views.register_business, name='register_business'),
    url(r'^accounts/my_profile/', views.my_profile, name='my_profile'),
    url(r'^accounts/hood_details/(?P<neighbourhood_id>\d+)',
        views.hood_details, name='hood_details'),
    url(r'^post-news/(?P<neighbourhood_id>\d+)',
        views.post_news, name='post_news'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
