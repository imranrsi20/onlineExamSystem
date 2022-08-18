
from django.urls import path
from questions import views


urlpatterns = [

    path('', views.home,name='home'),
    path('exam_home/',views.ExamHome,name='exam_home'),


]
