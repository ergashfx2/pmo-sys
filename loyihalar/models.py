import uuid

from django.db import models

from hodimlar.models import User
status_choices = (
    ('Yangi',"Yangi"),
    ('Jarayonda',"Jarayonda"),
    ('Tugatilgan',"Tugatilgan"),
)

class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, models.CASCADE,related_name='author')
    project_curator = models.ForeignKey(User,models.CASCADE,related_name='curator')
    project_name = models.CharField(max_length=200)
    project_description = models.TextField()
    project_done_percentage = models.CharField(max_length=20,default=0)
    project_start_date = models.DateTimeField(auto_now=True)
    project_deadline = models.DateField()
    project_budget = models.CharField(max_length=30)
    project_status = models.CharField(max_length=30,choices=status_choices,default='Yangi')
    project_spent_money = models.CharField(max_length=30,default=0)


    def update_project_done_percentage(self):
        self.project_done_percentage = str(self.project_done_percentage)
        self.save()

    def __str__(self):
        return self.project_name


class Phase(models.Model):
    project = models.ForeignKey(Project, models.CASCADE)
    phase_name = models.CharField(max_length=250)
    phase_done_percentage = models.CharField(max_length=20, default=0)

    def update_project_done_percentage(self):
        self.phase_done_percentage = str(self.phase_done_percentage)
        self.save()


    def update_project_name(self):
        self.phase_name = str(self.phase_name)
        self.save()

    def __str__(self):
        return self.phase_name


class Task(models.Model):
    project = models.ForeignKey(Project,models.CASCADE)
    phase = models.ForeignKey(Phase, models.CASCADE)
    task_name = models.CharField(max_length=250)
    task_done_percentage = models.CharField(max_length=20, default=0)

    def update_task_done_percentage(self):
        self.task_done_percentage = str(self.task_done_percentage)
        self.save()

    def update_task_name(self):
        self.task_name = str(self.task_name)
        self.save()

    def __str__(self):
        return self.task_name


class Documents(models.Model):
    project = models.ForeignKey(Project, models.CASCADE)
    document = models.FileField(upload_to='')

    def __str__(self):
        return self.project.project_name
