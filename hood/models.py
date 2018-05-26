from django.db import models
import datetime as dt

# Create your models here.

class Neighbourhood (models.Model):
    name = models.CharField(max_length = 60)
    location = models.CharField(max_length = 60)
    occupants_count = models.IntegerField()
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
        

class User (models.Model):
    name = models.CharField(max_length = 30)
    id_number = models.IntegerField()
    neighbourhood = models.ForeignKey(Neighbourhood)
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
    business_email = models.EmailField()

    def __str__(self):
        return self.business_name

    def save_Business(self):
        self.save()
    
    def delete_Business(self):
        self.delete()

    @classmethod
    def search_by_Business(cls,search_term):
        business = cls.objects.filter(image_category__name__icontains=search_term)
        return business
    