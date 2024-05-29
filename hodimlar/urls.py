from django.urls import path
from .views import login_view, logoutView, profileView

app_name = 'hodimlar'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logoutView, name='logout'),
    path('profile/', profileView, name='profile')
]
