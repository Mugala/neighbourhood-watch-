from django.test import TestCase
from .models import Neighbourhood, User_profile, Business, Announcement

# Create your tests here.


class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        self.hood = Neighbourhood(
            name='Elm court', location='Westlands', occupants_count=3, admin="ME")
        self.hood.save_Neighbourhood()

    def tearDown(self):
        Neighbourhood.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.hood, Neighbourhood))

        # Testing Save Method
    def test_save_method(self):
        hood = Neighbourhood.objects.all()
        self.assertTrue(len(hood) > 0)

    def test_delete_method(self):
        self.hood.delete_Neighbourhood()
        hood = Neighbourhood.objects.all()
        self.assertTrue(len(hood) == 0)

    def test_update_method(self):
        updated_rows = Neighbourhood.update_hood(
            self.hood.id, name='Elm court')
        self.assertTrue(updated_rows == 1)


class User_profileTestClass(TestCase):
    def setUp(self):
        self.neighbourhood = Neighbourhood(name="Westlands")
        self.neighbourhood.save()
        self.user = User_profile(name='Levi', id_number=78426824, neighbourhood=self.neighbourhood,
                                 post="We are haveing a meeting at 10pm", email="mugalalevi21@gmail.com", pub_date='2018-05-06')
        self.user.save_User()

    def tearDown(self):
        Neighbourhood.objects.all().delete()
        User_profile.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User_profile))

        # Testing Save Method
    def test_save_method(self):
        user = User_profile.objects.all()
        self.assertTrue(len(user) > 0)

    def test_delete_method(self):
        self.user.delete_User()
        user = User_profile.objects.all()
        self.assertTrue(len(user) == 0)


class BusinessTestClass(TestCase):
    def setUp(self):
        self.user = User_profile(name="Levi")
        self.user.save()
        self.neighbourhood = Neighbourhood(name="Westlands")
        self.neighbourhood.save()
        self.business1 = Business(business_name='KFC', user=self.user,
                                  neighbourhood=self.neighbourhood, business_email="KFc@gmail.com")
        self.business1.save_User()

    def tearDown(self):
        Neighbourhood.objects.all().delete()
        User_profile.objects.all().delete()
        Business.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.business1, Business))

        # Testing Save Method
    def test_save_method(self):
        biz = Business.objects.all()
        self.assertTrue(len(biz) > 0)

    def test_delete_method(self):
        self.biz.delete_Business()
        biz = Business.objects.all()
        self.assertTrue(len(biz) == 0)

    def test_search_Business(self):
        business = Business.search_by_business("KFC")
        self.assertTrue(business.first().id == self.business.id)
