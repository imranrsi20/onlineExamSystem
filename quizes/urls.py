
from django.urls import path
from .views import *
from quizes import views
app_name='quizes'

urlpatterns = [

    path('exam_home/', views.QuizListView,name='exam_home'),
    path('exam_home/<pk>/',views.quiz_view,name='quiz_view'),
    path('exam_home/<pk>/save/',views.save_quiz_view,name='quiz_save'),
    path('exam_home/<pk>/data/',views.quiz_data_view,name='quiz_data_view'),


]
