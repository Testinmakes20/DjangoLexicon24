from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<em>My Second App</em>")

def help(request):
    return render(request,'apptwo/help.html')

def profile(request):
    return render(request,'apptwo/profile.html')
