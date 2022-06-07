from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog_home(request):
    return render(request, "main/blog_home.html")

def blog_details(request):
    return render(request, "main/blog_details.html")

def profile(request):
    return render(request, "main/profile.html")

def contact_us(request):
    return render(request, "main/contact_us.html")