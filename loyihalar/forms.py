from django.contrib.auth import get_user_model
from django.forms import forms, ModelForm
from loyihalar.models import Project,status_choices
from .models import Documents
from django import forms
User = get_user_model()

class CreateProjectForm(ModelForm):
    project_name = forms.CharField(label="Loyiha nomi",max_length=200,widget=forms.TextInput(attrs={'class':'form-control'}))
    project_deadline = forms.DateField(label="Loyiha tugash sanasi",widget=forms.DateInput(attrs={'class':'form-control'}))
    project_description = forms.CharField(label="Loyiha haqida qisqacha yozing",max_length=400,widget=forms.Textarea(attrs={'class':'form-control'}))
    project_budget = forms.CharField(label="Loyiha uchun sarflanadigan pul miqdori",max_length=400,widget=forms.TextInput(attrs={'class':'form-control'}))
    project_curator = forms.ModelChoiceField(label="Loyiha kuratorini tanlang",queryset=User.objects,widget=forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model = Project
        fields = ['project_name', 'project_curator', 'project_deadline', 'project_description', 'project_budget']


class EditProjectForm(ModelForm):
    project_name = forms.CharField(label="Loyiha nomi",max_length=200,widget=forms.TextInput(attrs={'class':'form-control'}))
    project_deadline = forms.DateField(label="Loyiha tugash sanasi",widget=forms.DateInput(attrs={'class':'form-control'}))
    project_description = forms.CharField(label="Loyiha haqida qisqacha yozing",max_length=400,widget=forms.Textarea(attrs={'class':'form-control'}))
    project_budget = forms.CharField(label="Loyiha uchun sarflanadigan pul miqdori",max_length=150,widget=forms.TextInput(attrs={'class':'form-control'}))
    project_spent_money = forms.CharField(label="Loyiha uchun sarflangan pul miqdori",max_length=150,widget=forms.TextInput(attrs={'class':'form-control'}))
    project_curator = forms.ModelChoiceField(label="Loyiha kuratorini tanlang",queryset=User.objects,widget=forms.Select(attrs={'class':'form-control'}))
    project_status = forms.CharField(label="Loyiha statusi",widget=forms.Select(attrs={'class':'form-control'},choices=status_choices))
    class Meta:
        model = Project
        fields = ['project_name', 'project_curator', 'project_deadline', 'project_description', 'project_budget','project_spent_money','project_status']


class AddFileForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = ['document']
