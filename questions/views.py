from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    return render(request,'home.html')

def ExamHome(request):
    return render(request,'test4.html')