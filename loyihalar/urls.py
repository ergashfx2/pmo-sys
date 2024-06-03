from django.urls import path
from .views import all_projects,get_project
urlpatterns = [
    path('all/',all_projects,name='all-projects'),
    path('<pk>/',get_project,name='get-project')
]