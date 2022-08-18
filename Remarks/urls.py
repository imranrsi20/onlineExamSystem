
from django.urls import path
from Remarks import views


urlpatterns = [

    path('teacher_dashboard/',views.TeacherDashboard,name='t_dashboard'),

]
