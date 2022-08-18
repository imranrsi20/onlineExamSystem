from django.shortcuts import render
from .models import *
# Create your views here.

def TeacherDashboard(request):
    return render(request,'t_dashboard.html')