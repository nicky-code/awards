from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.shortcuts import render
from .models import Projects,Profile
from .forms import ProjectForm,ProfileForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/accounts/login/')
def welcome(request):
    
    project=Projects.objects.all()
    awards_users=Profile.objects.all()
    current_user = request.user
    myProfile = Profile.objects.filter(user = current_user).first()
    print(project)
    
    return render(request, 'welcome.html',{"project":project},"awards_users":awards_users,"myProfile":myProfile)


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


@login_required(login_url='/accounts/login/')
def search_titles(request):
    
   if 'title' in request.GET and request.GET["title"]:
       search_term = request.GET.get("title")
       searched_title = Projects.search_by_title(search_term)
       print(searched_title)
       message = f"{search_term}"
       return render(request, "all-awards/search.html",{"message":message,"titles": searched_title})
   else:
       message = "You haven't searched for any term"
       return render(request, 'all-awards/search.html',{"message":message})


@login_required(login_url='/accounts/login/')
def new_profile(request):
    
    current_user = request.user
    profil = Profile.objects.filter(id=current_user.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = current_user
            photo.save()
        return redirect('myProfile')

    else:
        form = ProfileForm()
    
    return render(request, 'new-profile.html',{"form":form})


@login_required(login_url='/accounts/login/')
def myProfile(request):
    
   current_user = request.user 
   all_projects = Projects.objects.filter(user=current_user)
   myProfile = Profile.objects.filter(user = current_user).first()
   return render(request, 'profile.html', {"all_projects":all_projects, "myProfile":myProfile})
