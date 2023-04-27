from django.shortcuts import render
from django.urls import reverse
from .models import Project
def projectview(request,pk):
    context ={
        'obj':Project.objects.get(id=pk)
    }
    return render(request,'comments.html', context = context)