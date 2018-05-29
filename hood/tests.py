from django.test import TestCase
from .models import Neighbourhood,User_profile,Business,Announcement

# Create your tests here.

class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        self.hood = Neighbourhood(name = 'Elm court', location = 'Westlands', occupants_count = 3, admin = "ME")
        self.hood.save_Neighbourhood()
    
    def tearDown(self):
        Announcement.objects.all().delete()
        User_profile.objects.all().delete()
        Business.objects.all().delete()
        Neighbourhood.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.hood,Neighbourhood))

             # Testing Save Method
    def test_save_method(self):
        hood = Neighbourhood.objects.all()
        self.assertTrue(len(hood) > 0)
         
        
    def test_delete_method(self):
        self.hood.delete_Neighbourhood()
        hood = Neighbourhood.objects.all()
        self.assertTrue(len(hood) == 0)

    def test_update_method(self):
        updated_rows = Neighbourhood.update_hood(self.hood.id, name = 'Elm court')
        self.assertTrue(updated_rows == 1)
 

    def test_search_Business(self):
        business = Business.search_by_business("KFC")
        self.assertTrue(business.first().id == self.business.id)
    
