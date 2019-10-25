from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.shortcuts import render
from .models import Projects
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/accounts/login/')
def welcome(request):
    
    project=Projects.objects.all()
    current_user = request.user
    
    return render(request, 'welcome.html',{"project":project})


@login_required(login_url='/accounts/login/')
def new_project(request):
    
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect('welcome')

    else:
        form = ProjectForm()
    
    return render(request, 'new_project.html',{"form":form})

