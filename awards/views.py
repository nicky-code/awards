from django.shortcuts import render
from django.http  import HttpResponse
from django.shortcuts import render
from .models import Projects,Profile

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')
