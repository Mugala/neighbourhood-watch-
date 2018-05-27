from django.contrib import admin
from .models import Neighbourhood, User,Business,User_profile
# Register your models here.


admin.site.register(Neighbourhood)
admin.site.register(User_profile)
admin.site.register(Business)