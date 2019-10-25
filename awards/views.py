from django.shortcuts import render
from django.http  import HttpResponse
from django.shortcuts import render
from .models import Projects,Profile
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/accounts/login/')
def welcome(request):
    return render(request, 'welcome.html')
