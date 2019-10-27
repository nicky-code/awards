from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.shortcuts import render
from .models import Projects,Profile
from .forms import ProjectForm,ProfileForm,VoteForm
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from .serializer import ProjectSerializer,ProfileSerializer
from rest_framework import status
from django.db.models import Max,F

# Create your views here.

@login_required(login_url='/accounts/login/')
def welcome(request):
    
    project=Projects.objects.all()
    awards_users=Profile.objects.all()
    current_user = request.user
    myProfile = Profile.objects.filter(user = current_user).first()
    print(project)
    
    average=0
    
    for proj in project:
        average = (proj.design + proj.usability + proj.content)/3
        best_rating = round(average,2)

    return render(request, 'welcome.html',{"project":project,"awards_users":awards_users,"myProfile":myProfile,'best_rating':best_rating'})


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


class ProjectsList(APIView):
    
    def get(self, request, format=None):
        all_projects = Projects.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)
    
    
class ProfileList(APIView):
    
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)


#I have Found this on github user="MaryannGitonga"
@login_required(login_url='/accounts/login/')
def rating(request,id):
    myProject=Projects.objects.get(id=id)
    rating = round(((myProject.design + myProject.usability + myProject.content)/3),1)
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid:
            myProject.submission_votes += 1
            if myProject.design == 0:
                myProject.design = int(request.POST['design'])
            else:
                myProject.design = (myProject.design + int(request.POST['design']))/2
            if myProject.usability == 0:
                myProject.usability = int(request.POST['usability'])
            else:
                myProject.usability = (myProject.design + int(request.POST['usability']))/2
            if myProject.content == 0:
                myProject.content = int(request.POST['content'])
            else:
                myProject.content = (myProject.design + int(request.POST['content']))/2
            myProject.save()
            return redirect('welcome')
    else:
        form = VoteForm()
    return render(request,'vote.html',{'form':form,'myProject':myProject,'rating':rating})    