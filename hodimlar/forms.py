from django import forms
from django.contrib.auth.models import User


class CreateUserForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput({'placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput({'placeholder': 'Parol'}))
    password2 = forms.CharField(widget=forms.PasswordInput({'placeholder': 'parolni qayta kiriting'}))

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if self.password1 != self.password2:
            self.add_error('password1', "Ikkala parol bir xil bo'lishi kerak")
            self.add_error('password2', "Ikkala parol bir xil bo'lishi kerak")

        if len(str(self.username)) > 150:
            self.add_error('username', "Username 150 belgidan ko'p bo'lishi mumkin emas ")


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(max_length=150, widget=forms.PasswordInput(attrs={'placeholder': 'Parol'}))

