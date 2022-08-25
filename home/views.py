from django.shortcuts import render
from django.urls import reverse

# Create your views here.


def home_view(request):
    # return HttpResponse("Hello ")
    return render(request, 'home_page.html')
