from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class NewsLetterRecipient (models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()

class Neighbourhood (models.Model):
    name = models.CharField(max_length = 60)
    location = models.CharField(max_length = 60)
    occupants_count = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
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
    neighbourhood = models.OneToOneField(Neighbourhood, null=True)
    post = HTMLField()
    email = models.EmailField()
    pub_date= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save_User(self):
        self.save()
    
    def delete_User(self):
        self.delete()

    @classmethod
    def user_details(cls):
        user_details = cls.objects.all()
        return user_details

class Business (models.Model):
    business_name = models.CharField(max_length = 30)
    user = models.ForeignKey(User)
    neighbourhood = models.OneToOneField(Neighbourhood)
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
    
class Announcement (models.Model):
    news = models.TextField(blank=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
   

    def __str__(self):
        return self.news

    @classmethod
    def get_news(cls, neighbourhood_id):
        news = cls.objects.filter(neighbourhood=neighbourhood_id)
        return news