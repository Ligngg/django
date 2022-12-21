
from django.shortcuts import render
from django.http import HttpResponse
from .models import taskdjango


# Create your views here.

def home(request):
    ob=taskdjango.objects.all()


    return render(request,"index.html",{"res":ob})

