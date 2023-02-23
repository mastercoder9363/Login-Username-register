from django.contrib import admin
from django.urls import path
from core.views import *
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.LoginView.as_view(template_name="login3.html")),
    path('index/', index, name="index")
]
