from django.shortcuts import render
from .models import *
from questions import views
from django.http import JsonResponse
from django.views.generic import ListView
from questions.models import *
from results.models import *
from accounts.models import *
# Create your views here.


def QuizListView(request):
    quiz_obj=Quiz.objects.all()

    context={
        "object_list":quiz_obj,

    }
    return render(request,'quiz/exam_home_page.html',context)
def quiz_view(request,pk):
    quiz=Quiz.objects.get(pk=pk)
    current_user = request.user
    check = Result.objects.filter(user__username = current_user,quiz__pk = pk)
    l = len(check)

    context={
        'obj':quiz,
        'length':l,
    }
    return render(request,'quiz/quiz.html',context)

def quiz_data_view(request,pk):
    quiz = Quiz.objects.get(pk=pk)
    questions=[]
    for q in quiz.get_questions():
        answers=[]
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q):answers})

    return JsonResponse({
        'data':questions,
        'time':quiz.time,
    })


def save_quiz_view(request,pk):
    if request.is_ajax():
        questions=[]
        data=request.POST
        data_=dict(data.lists())
        data_.pop('csrfmiddlewaretoken')

        for k in data_.keys():
            question=Question.objects.get(text=k)
            questions.append(question)
        user=request.user
        s_n = ""
        s_id= ""
        student_obj = Student.objects.filter(user__username=user)
        for s in student_obj:
            s_n=s.name
            s_id=s.student_id
        quiz=Quiz.objects.get(pk=pk)
        score=0
        multiplier=100/quiz.number_of_questions
        results = []
        correct_answer = None

        for q in questions:
            selected_ans=request.POST.get(q.text)
            #print('selected :',selected_ans)
            if selected_ans != "":
                question_answers = Answer.objects.filter(question=q)
                for a in question_answers:
                    if selected_ans == a.text:
                        if a.correct:
                            score += 1
                            correct_answer = a.text
                    else:
                        if a.correct:
                            correct_answer = a.text
                results.append({str(q):{'correct_answer':correct_answer,'answered':selected_ans}})
            else:
                results.append({str(q): 'not answered'})
        score_ = score*multiplier
        Result.objects.create(quiz=quiz,user=user,student_name=s_n,Student_id=s_id,score=score_)

        if score_ >= quiz.required_score_to_pass:
            return JsonResponse({'passed':True,'score':score_,'results':results})
        else:
            return JsonResponse({'passed': False,'score':score_,'results':results})
