from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('register/', register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name='people/logout.html'), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='people/login.html'), name='login'),

]
