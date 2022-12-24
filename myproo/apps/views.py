from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from myproo.form import productForm
from.models import product

# Create your views here.
def index(request):
    if request.method=='POST':
        form=productForm(request.post)
        if form.is_valid():
           form.save()
           return HttpResponse("saved successfully")
        else:
            return HttpResponse("error")
    else:
        form=productForm()
        return render(request,'index.html',{"form":productForm})