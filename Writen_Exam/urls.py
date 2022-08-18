
from django.urls import path
from Writen_Exam import views


urlpatterns = [

    path('writen_exam/',views.Writen_Exam_Home,name='writen_exam'),
    #path('writen_exam/<pk>/',views.Writen_Exam_Home_Data,name='writen_exam_data'),
    path('writen_exam/<pk>/save/', views.W_Q_A_save, name='w_q_a_save'),
    path('writen_exam/<pk>/data/', views.W_Q_data_view, name='w_q_data_view'),

    path('writen_exam/<pk>/',views.QuestionPaper,name='writen_exam_data'),
    path('saveans/',views.SaveAns,name='saveans'),
    path('submit_exam/',views.SubmitExam,name='submitexam'),

]
