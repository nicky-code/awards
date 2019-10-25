from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length =30)
    image = models.ImageField(upload_to ='images/',null=True)
    project_description = models.CharField(max_length=250)
    link = models.CharField(max_length =30)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.projects
    
    
    def save_projects(self):
        self.save()
    
    def delete_projects(self):
        self.delete()
        
    def update_projects(self):
        self.update()
    

class Profile(models.Model):
    profile_picture = models.ImageField(upload_to ='pictures/',null=True)
    bio = models.CharField(max_length=30,null=True)
    posted_projects = models.TextField()
    user_contact= models.CharField(max_length=30,null=True)
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.profile
    
    
    def save_profile(self):
        self.save()
    
    def delete_profile(self):
        self.delete()
        
    def update_profile(self):
        self.update()
        
        
