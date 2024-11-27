"""
URL configuration for GoFinal project.

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
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('service/', views.service, name='service'),
    path('starter/', views.starter,name='starter'),
    path('about/', views.about,name='about'),
    path('doctors/', views.doctors,name='doctors'),
    path('myservice/', views.myservice,name='myservice'),
    path('appointment/', views.appointment,name='appointment'),
    path('show/', views.show,name='show'),
    path('delete/<int:id>', views.delete),
    path('contact/', views.contact,name='contact'),
    path('show_contact/', views.show_contact),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update, name='update'),
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('uploadimage/', views.upload_image, name='upload'),
    path('showimage/', views.show_image, name='image'),

    #Mpesa API urls
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),
]
