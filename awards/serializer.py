from rest_framework import serializers
from .models import Projects,Profile

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('title', 'image', 'project_description', 'link')
        
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('profile_picture', 'bio', 'posted_projects', 'user_contact')