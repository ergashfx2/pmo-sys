from django.urls import path
from .views import login_view, logoutView, profileView, UserUpdateView, UsersView, create_user

app_name = 'hodimlar'

urlpatterns = [
    path('view/', UsersView.as_view(), name='users'),
    path('login/', login_view, name='login'),
    path('logout/', logoutView, name='logout'),
    path('profile/', profileView, name='profile'),
    path('create-user/', create_user, name='create-user'),
    path('update/<pk>', UserUpdateView.as_view(), name='update-user'),
]
