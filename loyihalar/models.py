import uuid

from django.db import models

from hodimlar.models import User

class Phase(models.Model):
    phase_name = models.CharField(max_length=250)
    phase_done_percentage = models.CharField(max_length=20, default=0)

    def __str__(self):
        return self.phase_name


class Task(models.Model):
    phase = models.ForeignKey(Phase, models.CASCADE)
    task_name = models.CharField(max_length=250)
    task_done_percentage = models.CharField(max_length=20, default=0)

    def __str__(self):
        return self.task_name


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, models.CASCADE)
    project_curator = models.CharField(max_length=250)
    project_name = models.CharField(max_length=200)
    project_description = models.TextField()
    project_done_percentage = models.CharField(max_length=20)
    project_start_date = models.DateTimeField(auto_now=True)
    project_deadline = models.DateTimeField()
    project_budget = models.CharField(max_length=30)
    project_spent_money = models.CharField(max_length=30)
    project_documents = models.FileField(upload_to='files/')
    project_steps = models.ForeignKey(Phase, models.CASCADE)
    step_tasks = models.ForeignKey(Task, models.CASCADE)

    def __str__(self):
        return self.project_name


class Documents(models.Model):
    project = models.ForeignKey(Project, models.CASCADE)
    document = models.FileField(upload_to='files')

    def __str__(self):
        return self.document
