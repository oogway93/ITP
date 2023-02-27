from django.urls import path,include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('myblog.urls')),
    path('', include('people.urls')),



]
