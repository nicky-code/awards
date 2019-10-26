from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^search/',views.search_titles, name = 'searchs'),
    url(r'^new/new_project$',views.new_project,name = 'new_project'),
    url(r'^new/profile$',views.new_profile,name = 'profile'),
    url(r'^myProfile$',views.myProfile,name = 'myProfile'),
    url(r'^api/project/$', views.ProjectsList.as_view(),name='project'),
    url(r'^api/profile/$', views.ProfileList.as_view(),name='profil'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)