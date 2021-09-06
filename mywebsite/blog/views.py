from django.shortcuts import render,redirect
from . import models
from . import  forms
# Create your views here.


def list(request):
    model = models.postmodel.objects.all()
    context ={
        'models' :model
    }
    return render(request,'list.html',context)


def create(request):
    form = forms.postforms(request.POST or None)
    if request.method =='POST':
        if form.is_valid():
            form.save()
        return redirect('list')
    context ={
        'forms' :form
    }
    return render(request,'create.html',context)


