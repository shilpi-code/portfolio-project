from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
# Create your views here.
def home(request):
    detail= Project.objects.all()
    return render(request,'intro.html', {'projects':detail})