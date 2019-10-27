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
        self.title.save_projects()
        title=Projects.objects.all()
        self.assertTrue(len(title)>=1)
           