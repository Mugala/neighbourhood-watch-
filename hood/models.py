from django.db import models
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.

class NewsLetterRecipient (models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()

class Neighbourhood (models.Model):
    name = models.CharField(max_length = 60)
    location = models.CharField(max_length = 60)
    occupants_count = models.IntegerField(null=True)
    admin = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.name

    def save_Neighbourhood (self):
        self.save()

    def delete_Neighbourhood(self):
        self.delete()

    @classmethod
    def neighbourhood_details(cls):
        details = cls.objects.all()
        return details
        

class User_profile (models.Model):
    name = models.CharField(max_length = 30)
    id_number = models.IntegerField()
    neighbourhood = models.ForeignKey(Neighbourhood, null=True)
    email = models.EmailField()

    def __str__(self):
        return self.name

    def save_User(self):
        self.save()
    
    def delete_User(self):
        self.delete()

class Business (models.Model):
    business_name = models.CharField(max_length = 30)
    user = models.ForeignKey(User)
    neighbourhood = models.ForeignKey(Neighbourhood)
    business_image = models.ImageField(upload_to = 'biz-image/', null= True)
    business_email = models.EmailField()

    def __str__(self):
        return self.business_name

    def save_Business(self):
        self.save()
    
    def delete_Business(self):
        self.delete()

    @classmethod
    def search_by_business(cls,search_term):
        business = cls.objects.filter(business_name__icontains=search_term)
        return business
    