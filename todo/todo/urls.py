"""
URL configuration for todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth.urls import views as auth_view
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    #coustomized folder name 'register'
    #path('',LoginView.as_view(template_name='register/login.html'),name='login_page'),
    path('',views.todo_list,name='todo_list'),
    path('<int:task_id>/update/',views.edit_todo,name='update'),
    path('<int:task_id>/delete/',views.delete_todo,name='delete'),
    path('accounts/',include('django.contrib.auth.urls')),
    
    #register
    path('register/',views.register,name='register'),
    
    
    path("__reload__/", include("django_browser_reload.urls")),
]
