from django.urls import path
from .import views

app_name='blog' 
urlpatterns=[
    path('', views.folder,name='folder'),
    path('<int:bloggg_id>/',views.func,name='func'),
    
]
