from django.urls import path
from .import views
from .import templates

urlpatterns=[
    path('',views.home,name='home')
]