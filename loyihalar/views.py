from uuid import UUID

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Project, Phase, Task, Documents


@login_required
def all_projects(request):
    projects = Project.objects.all()
    phases = Phase.objects.all()
    tasks = Task.objects.all()
    return render(request, 'all_projects.html', context={'projects': projects, 'phases': phases, 'tasks': tasks})


@login_required
def get_project(request, pk):
    project = Project.objects.filter(pk=pk)
    datas = []
    phases = Phase.objects.filter(project_id=project[0].id)
    for phase in phases:
        datas.append({
            'phase': phase.phase_name,
            'phase_done_percentage' : int(phase.phase_done_percentage),
            'tasks': Task.objects.filter(phase=phase.id)
        })
    print(datas)
    documents = Documents.objects.filter(project=project[0].id)
    return render(request, 'project_detail.html', context={'project': project, 'datas': datas, 'documents': documents})
