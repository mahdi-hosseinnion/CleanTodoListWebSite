from django.shortcuts import render

# Create your views here.

def home_screan_view(request):
    return render(request,"base.html",{})
