from django import forms
from .models import Neighbourhood,Business,User


class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

class NeighbourhoodDetails (forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = ['name', 'location', 'admin',]
        exclude = ['occupants_count',]


class BusinessDetails (forms.ModelForm):
    class Meta:
        model = Business
        fields = ['business_name', 'business_email', 'business_image',]
        exclude = ['neighbourhood', 'user']
     

class UserProfile (forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'id_number', 'email',]
        exclude = ['neighbourhood',]

