from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Neighbourhood,Business,User,NewsLetterRecipient
from .forms import NewsLetterForm,NeighbourhoodDetails,BusinessDetails,UserProfile
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required

# Create your views here.

def welcome (request):    
    return render(request, "welcome.html")

@login_required(login_url='/accounts/login/')
def home(request):    
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipient(name = name,email =email)
            recipient.save()

            recipient = NewsLetterRecipient(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)

            HttpResponseRedirect('home')
    else:
        form = NewsLetterForm()
    return render(request, "home.html", {"letterForm":form})

def user_profile(request):  
    current_user = request.user
    if request.method =='POST':
        form = UserProfile(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()

            return redirect("home")
    else:
        form = UserProfile()
    return render (request, 'all-updates/user_profile.html',{"form":form})

# def register_car(request):  
#     current_user = request.user
#     if request.method =='POST':
#         form = CarDetails(request.POST, request.FILES)
#         if form.is_valid():
#             carProfile = form.save(commit=False)
#             carProfile.user = current_user
#             carProfile.save()

#             return redirect("dwelcome")
#     else:
#         carform = CarDetails()
#     return render (request, 'dtemp/car_profile.html',{"carform":carform})
    
def search_results(request):

    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_business = Business.search_by_business(search_term)
        results = [*searched_business]
        message = f"{search_term}"

        return render(request, 'all-updates/search.html',{"message":message,"businesses": results})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-updates/search.html',{"message":message})

