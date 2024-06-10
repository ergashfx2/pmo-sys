import json
import uuid

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView

from .forms import CreateProjectForm, EditProjectForm, AddFileForm, AddPhaseForm, AddTaskForm
from .formsets import TaskFormSet
from .models import Project, Phase, Task, Documents
file_extensions = {
    'ai': 'adobe',
    'avi': 'film',
    'bmp': 'file-image',
    'css': 'css3',
    'csv': 'file-csv',
    'doc': 'file-word',
    'docx': 'file-word',
    'eps': 'file-image',
    'exe': 'file-code',
    'flv': 'film',
    'gif': 'file-image',
    'html': 'html5',
    'ico': 'file-image',
    'iso': 'file-archive',
    'jpg': 'file-image',
    'jpeg': 'file-image',
    'js': 'js',
    'mp3': 'file-audio',
    'mp4': 'film',
    'pdf': 'file-pdf',
    'png': 'file-image',
    'ppt': 'powerpoint',
    'pptx': 'powerpoint',
    'psd': 'adobe',
    'rar': 'file-archive',
    'svg': 'file-image',
    'tif': 'file-image',
    'tiff': 'file-image',
    'txt': 'file-alt',
    'wav': 'file-audio',
    'xls': 'file-excel',
    'xlsx': 'file-excel',
    'xml': 'code',
    'zip': 'file-archive'
}


@login_required
def all_projects(request):
    projects = Project.objects.all()
    phases = Phase.objects.all()
    tasks = Task.objects.all()
    return render(request, 'all_projects.html', context={'projects': projects, 'phases': phases, 'tasks': tasks})


@login_required
def myProjects(request):
    projects = Project.objects.filter(author=request.user.pk)
    return render(request, 'my-projects.html', context={'projects': projects})


@login_required
def get_project(request, pk):
    project = Project.objects.filter(pk=pk)
    datas = []
    form = AddFileForm
    phases = Phase.objects.filter(project_id=project[0].id)
    for phase in phases:
        datas.append({
            'phase': phase.phase_name,
            'phase_done_percentage': int(phase.phase_done_percentage),
            'tasks': Task.objects.filter(phase=phase.id)
        })
    documents = Documents.objects.filter(project=project[0].id)
    return render(request, 'project_detail.html', context={'project': project, 'datas': datas, 'documents': documents})


@login_required
def DetailMyProjects(request, pk):
    form = AddFileForm()
    form2 = AddPhaseForm()
    form3 = TaskFormSet()
    project = Project.objects.filter(pk=pk)
    datas = []
    phases = Phase.objects.filter(project_id=project[0].id)
    for phase in phases:
        datas.append({
            'phase': phase.phase_name,
            'phase_id': phase.pk,
            'phase_done_percentage': int(phase.phase_done_percentage),
            'tasks': Task.objects.filter(phase=phase.id)
        })

    #saving document
    if request.method == 'POST':
        form = AddFileForm(data=request.POST, files=request.FILES)
        if form.is_valid() and form.cleaned_data.get('document'):
            document = form.save(commit=False)
            doc_type = str(form.cleaned_data.get('document')).split('.')[-1]
            document.document = form.cleaned_data.get('document')
            document.type = file_extensions[doc_type]
            document.project = Project.objects.get(pk=pk)
            document.save()
            redirect('my-projects-detail', pk=pk)
        if form.is_valid() and form.cleaned_data.get('url'):
            document = form.save(commit=False)
            url = str(form.cleaned_data.get('url'))
            document.type = 'link'
            document.url = url
            document.project = Project.objects.get(pk=pk)
            document.save()
            redirect('my-projects-detail',pk=pk)

        formPhase = AddPhaseForm(request.POST)
        if formPhase.is_valid():
            new_phase = formPhase.save(commit=False)
            new_phase.project = project
            new_phase.save()
            task_formset = TaskFormSet(request.POST, instance=new_phase)
            if task_formset.is_valid():
                task_formset.save()
                redirect('my-projects-detail',pk=pk)
        redirect('my-projects-detail',pk=pk)

    #end saving document

    documents = Documents.objects.filter(project=project[0].id).order_by('created_at')
    return render(request, 'my-projects-detail.html',
                  context={'project': project, 'datas': datas, 'documents': documents, 'form': form, 'form2': form2,
                           'form3': form3})


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

    return render(request, 'create_project.html', context={'form': form})


class UpdateProject(UpdateView):
    model = Project
    template_name = 'update_project.html'
    form_class = EditProjectForm

    def get_success_url(self):
        return reverse('my-projects')


@login_required
def DeleteProject(request, pk):
    project = Project.objects.select_related(pk).filter(pk=pk)
    project.delete()
    return redirect('my-projects')


@login_required
def add_phase(request,pk):
    data = json.loads(request.body)
    phase = Phase.objects.create(phase_name=data['phase_name'],project_id=pk)
    for task in data['tasks']:
        Task.objects.create(project_id=pk,phase_id=phase.id,task_name=task)
    return render(request,template_name='my-projects-detail.html')


@login_required
def update_phase(request,pk):
    if request.method == 'POST':
        data = json.loads(request.body)
        Phase.objects.select_related(pk).filter(pk=pk).update(phase_name=data['phase_name'])
        return redirect('my-projects')
    return redirect('my-projects')


@login_required
def delete_phase(request,pk):
        Phase.objects.select_related(pk).filter(pk=pk).delete()
        return redirect('my-projects')


@login_required
def update_task(request,pk):
    if request.method == 'POST':
        data = json.loads(request.body)
        Task.objects.select_related(pk).filter(pk=pk).update(task_name=data['task_name'])
        return redirect('my-projects')
    return redirect('my-projects')


@login_required
def update_task_percentage(request,pk):
    if request.method == 'POST':
        data = json.loads(request.body)
        Task.objects.select_related(pk).filter(pk=pk).update(task_done_percentage=data['task_done_percentage'])
        phase = Task.objects.filter(pk=pk).values()[0]['phase_id']
        tasks = Task.objects.filter(phase_id=phase)
        phase_done_percentage = 0
        project_done_percentage = 0
        for task in tasks:
            phase_done_percentage += int(task.task_done_percentage)
        final_phase_percentage = phase_done_percentage / len(tasks)
        print(final_phase_percentage)
        phase_obj = Phase.objects.get(pk=phase)
        phase_obj.phase_done_percentage = int(final_phase_percentage)
        phase_obj.save()
        phases = Phase.objects.filter(project_id=phase_obj.project.id)
        for phase in phases :
            project_done_percentage += int(phase.phase_done_percentage)
        final_project_percentage = project_done_percentage / len(phases)
        project_obj = Project.objects.get(pk=phase_obj.project.id)
        print(final_project_percentage)
        project_obj.project_done_percentage = int(final_project_percentage)
        project_obj.save()
        return redirect('my-projects')
    return redirect('my-projects')


@login_required
def delete_task(request,pk):
        Task.objects.select_related(pk).filter(pk=pk).delete()
        return redirect('my-projects')