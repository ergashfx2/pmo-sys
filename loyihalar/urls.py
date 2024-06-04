from django.urls import path
from .views import all_projects,get_project,myProjects,DetailMyProjects
urlpatterns = [
    path('all/',all_projects,name='all-projects'),
    path('my-projects/',myProjects,name='my-projects'),
    path('my-projects/edit/<pk>',myProjects,name='my-projects'),
    path('my-projects/add-file/<pk>',myProjects,name='my-projects'),
    path('my-projects/delete/<pk>',myProjects,name='my-projects'),
    path('my-projects/detail/<pk>',DetailMyProjects,name='my-projects-detail'),
    path('<pk>/',get_project,name='get-project')
]