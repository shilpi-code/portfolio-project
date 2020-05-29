from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import myblog
# Create your views here.
def folder(request):
    detail= myblog.objects.order_by('-date')
    return render(request,'allblog.html', {'blogging':detail})

def func(request,bloggg_id):
    blog=get_object_or_404(myblog,pk=bloggg_id) #if that blog with the given id doesnot exist,show 404 error
    return render(request,'detail.html', {'blog':blog})

