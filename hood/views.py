from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Neighbourhood,Business,User,NewsLetterRecipient,User_profile
from .forms import NewsLetterForm,NeighbourhoodDetails,BusinessDetails,UserProfile,NewAnnouncementForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required

# Create your views here.

def welcome (request):    
    return render(request, "welcome.html")

@login_required(login_url='/accounts/login/')
def home(request):
    hood_details = Neighbourhood.neighbourhood_details()    
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
    return render(request, "home.html", {"hood_details":hood_details, "letterForm":form})

def user_profile(request):  
    current_user = request.user
    if request.method =='POST':
        form = UserProfile(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()

            return redirect("hood_profile")
    else:
        form = UserProfile()
    return render (request, 'all-updates/user_profile.html',{"form":form})

def register_hood(request):  
    current_user = request.user
    if request.method =='POST':
        form = NeighbourhoodDetails(request.POST, request.FILES)
        if form.is_valid():
            hood_Profile = form.save(commit=False)
            hood_Profile.user = current_user
            hood_Profile.save()

            return redirect("home")
    else:
        hoodform = NeighbourhoodDetails()
    return render (request, 'all-updates/hood_profile.html',{"hoodform":hoodform})


def register_business(request):  
    current_user = request.user
    if request.method =='POST':
        form = BusinessDetails(request.POST, request.FILES)
        if form.is_valid():
            business_Profile = form.save(commit=False)
            business_Profile.user = current_user
            business_Profile.save()

            return redirect("home")
    else:
        businessform = BusinessDetails()
    return render (request, 'all-updates/business_profile.html',{"businessform":businessform})


@login_required(login_url='/accounts/login/')
def my_profile(request):
    user_details = User_profile.user_details()
    hood_details = Neighbourhood.neighbourhood_details() 


    return render(request, 'all-updates/user_account.html',{"user_details":user_details,'hood_details':hood_details,})




@login_required(login_url='/accounts/login/')
def hood_details(request):
    details = Neighbourhood.neighbourhood_details()


    return render(request, 'all-updates/hood_posts.html',{"details":details,}) 



@login_required(login_url='/accounts/login/')
def post_news(request, neighbourhood_id):
    current_user = request.user
    announcement = get_object_or_404(Neighbourhood, id=neighbourhood_id)

    if request.method == 'POST':
        news_form = NewAnnouncementForm(request.POST)
        if news_form.is_valid():
            news = news_form.save(commit=False)
            news.image = announcement
            news.user = current_user
            news.save()
            return redirect("home")
            
    else:
        news_form = NewAnnouncementForm()

    return render(request, 'all-updates/news.html', {"form":news_form, "neighbourhood_id": neighbourhood_id})


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

