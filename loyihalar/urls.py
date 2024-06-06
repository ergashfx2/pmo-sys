from django.urls import path
from .views import all_projects,get_project,myProjects,DetailMyProjects,CreateProject,UpdateProject,DeleteProject,add_phase,update_phase
urlpatterns = [
    path('all/',all_projects,name='all-projects'),
    path('my-projects/',myProjects,name='my-projects'),
    path('my-projects/edit/<pk>',UpdateProject.as_view(),name='update-project'),
    path('my-projects/add-file/<pk>',myProjects,name='add-file'),
    path('my-projects/delete/<pk>',DeleteProject,name='delete-my-project'),
    path('my-projects/detail/<pk>/add-phase/', add_phase, name='add-phase'),
    path('my-projects/detail/<pk>',DetailMyProjects,name='my-projects-detail'),
    path('my-projects/detail/update-phase/<pk>',update_phase,name='update-phase'),
    path('my-projects/create/',CreateProject,name='create-project'),
    path('<pk>/',get_project,name='get-project')
]