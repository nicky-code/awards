from django.test import TestCase
from .models import Projects,Profile
from django.contrib.auth.models import User

# Create your tests here.
class ProjectsTestClass(TestCase):
    '''
    a class to test the projects instances and its methods
    '''

    # Set up method
    def setUp(self):
        self.user = User.objects.create(id=1,username='nicky')
        self.projects= Projects(title='Sodo-Ni Pizzeria',image='',project_description='Our favorites Pizzas', link='https://nicky-code.github.io/PizzaLover/',design='7',usability='8',content='7',user=self.user)
    
    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.projects,Projects))
        
    
    #Testing the save method
    '''
    function to check the save method of Projects
    '''
    
    def test_save_method(self):
        
        self.projects.save_projects()
        projects =Projects.objects.all()
        self.assertTrue(len(projects)>0)
       
    
    #Testing the delete method
    def test_delete_method(self):
        '''
        function to check the delete method of projects
        '''
        self.projects.save_projects()
        projected= Projects.objects.filter(title='Sodo-Ni Pizzeria').first()
        delete= Projects.objects.filter(id=projected.id).delete()
        project=Projects.objects.all()
        self.assertFalse(len(project)==1)


class ProfileTestClass(TestCase):
    '''
    a class to test the profile instances and its methods
    '''

    # Set up method
    def setUp(self):
        self.user = User.objects.create(id=1,username='nicky')
        self.projects= Projects(title='Sodo-Ni Pizzeria',image='',project_description='Our favorites Pizzas', link='https://nicky-code.github.io/PizzaLover/',design='7',usability='8',content='7',user=self.user)
        self.profile= Profile(profile_picture='',bio='alinenicole',user=self.user)
    
    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))
        self.assertTrue(isinstance(self.projects,Projects))
        
    
    #Testing the save method
    '''
    function to check the save method of Profile
    '''
    
    def test_save_method(self):
        self.profile.save_profile()
        profile =Profile.objects.all()
        self.assertTrue(len(profile)>0)

           
    #Testing the delete method
    def test_delete_method(self):
        '''
        function to check the delete method of profile
        '''
        self.profile.save_profile()
        profil= Profile.objects.filter(profile_picture='').first()
        delete= Profile.objects.filter(id=profil.id).delete()
        profile =Profile.objects.all()
        self.assertFalse(len(profile)==1)