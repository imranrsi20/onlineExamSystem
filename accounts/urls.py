from django.urls import path
from accounts import views


urlpatterns = [

    path('account/', views.account,name='account'),
    path('teacher_signup/',views.Teacher_signup,name='teacher_signup'),
    path('student_signup/',views.Student_signup,name='student_signup'),
    path('login/',views.Login,name='login'),
    path('logout/',views.Logout,name='logout'),
    path('test/',views.test,name='test'),



]