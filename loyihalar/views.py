from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView,DetailView,DeleteView,UpdateView

from .forms import CreateProjectForm,EditProjectForm,AddFileForm,AddPhaseForm,AddTaskForm
from .models import Project, Phase, Task, Documents

@login_required
def all_projects(request):
    projects = Project.objects.all()
    phases = Phase.objects.all()
    tasks = Task.objects.all()
    return render(request, 'all_projects.html', context={'projects': projects, 'phases': phases, 'tasks': tasks})



@login_required
def myProjects(request):
    projects = Project.objects.filter(author=request.user.pk)
    return render(request,'my-projects.html',context={'projects': projects})

@login_required
def get_project(request, pk):
    project = Project.objects.filter(pk=pk)
    datas = []
    form = AddFileForm
    phases = Phase.objects.filter(project_id=project[0].id)
    for phase in phases:
        datas.append({
            'phase': phase.phase_name,
            'phase_done_percentage' : int(phase.phase_done_percentage),
            'tasks': Task.objects.filter(phase=phase.id)
        })
    documents = Documents.objects.filter(project=project[0].id)
    return render(request, 'project_detail.html', context={'project': project, 'datas': datas, 'documents': documents})



@login_required
def DetailMyProjects(request,pk):
    form = AddFileForm
    form2 = AddPhaseForm
    form3 = AddTaskForm
    project = Project.objects.filter(pk=pk)
    datas = []
    phases = Phase.objects.filter(project_id=project[0].id)
    for phase in phases:
        datas.append({
            'phase': phase.phase_name,
            'phase_done_percentage' : int(phase.phase_done_percentage),
            'tasks': Task.objects.filter(phase=phase.id)
        })

     #saving document
    if request.method == 'POST':
        form = AddFileForm(data=request.POST,files=request.FILES)
        if form.is_valid() and form.cleaned_data.get('document'):
            document = form.save(commit=False)
            document.project = Project.objects.get(pk=pk)
            document.save()

        if form.is_valid() and form.cleaned_data.get('document'):
            document = form.save(commit=False)
            document.project = Project.objects.get(pk=pk)
            document.save()

    #end saving document




    documents = Documents.objects.filter(project=project[0].id)
    return render(request, 'my-projects-detail.html', context={'project': project, 'datas': datas, 'documents': documents,'form':form,'form2':form2,'form3':form3})

@login_required
def CreateProject(request):
    form = CreateProjectForm()
    if request.method == 'POST':
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = request.user
            project.save()
            return redirect('my-projects')


    return render(request,'create_project.html',context={'form':form})


class UpdateProject(UpdateView):
    model = Project
    template_name = 'update_project.html'
    form_class = EditProjectForm

    def get_success_url(self):
        return reverse('my-projects')


@login_required
def DeleteProject (request,pk):
    project = Project.objects.filter(pk=pk)
    project.delete()
    return redirect('my-projects')
