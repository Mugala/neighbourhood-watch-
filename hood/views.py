from django.shortcuts import render
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Neighbourhood,Business,User,NewsLetterRecipient
from .forms import NewsLetterForm

# Create your views here.

def home(request):    
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipient(name = name,email =email)
            recipient.save()
            HttpResponseRedirect('home')
    else:
        form = NewsLetterForm()
    return render(request, "home.html", {"letterForm":form})

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

