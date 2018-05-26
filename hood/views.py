from django.shortcuts import render
from django.http import HttpResponse
from .models import Neighbourhood,Business,User

# Create your views here.

def home(request):
    return render(request, "home.html")

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

