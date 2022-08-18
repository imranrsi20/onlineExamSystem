from django.shortcuts import render,HttpResponse
from .models import *
from writing_question.models import *
from django.core.paginator import Paginator,Page
from accounts.models import *
from Remarks.models import *
from django.http import JsonResponse
# Create your views here.

def Writen_Exam_Home(request):
    exam_obj = ExamInfo.objects.all()

    context = {
        "object_list": exam_obj,

    }
    return render(request,'WEHome.html',context)

def Writen_Exam_Home_Data(request,pk):
    subject=ExamInfo.objects.get(pk=pk)
    current_user = request.user
    check = W_Result.objects.filter(user__username = current_user,exam__pk = pk)
    l = len(check)

    context={
        'obj':subject,
        'length':l,
    }
    return render(request,'writenExam.html',context)

def W_Q_data_view(request,pk):
    quiz = ExamInfo.objects.get(pk=pk)
    questions=[]
    for q in quiz.get_questions():
        answers=[]
        for a in q.get_answers():
            answers.append(a.answer)
        questions.append({str(q):answers})

    return JsonResponse({
        'data':questions,
        'time':quiz.time,
    })


def W_Q_A_save(request,pk):
    if request.is_ajax():
        user = request.user.username
        questions = []
        data = request.POST
        data_ = dict(data.lists())
        data_.pop('csrfmiddlewaretoken')
        subject=""
        mark=0.0
        sub=ExamInfo.objects.filter(pk=pk)
        for s in sub:
            subject=s.subject

        for k in data_.keys():
            question = W_Question.objects.get(question=k)
            questions.append(question)

        for i in questions:
            answer=request.POST.get(i.question)
            Evaluate.objects.create(user=user,subject=subject,question=i,answer=answer,mark=mark)



        s_n = ""
        s_id = ""
        student_obj = Student.objects.filter(user__username=user)
        for s in student_obj:
            s_n = s.name
            s_id = s.student_id

    return HttpResponse("save")


def QuestionPaper(request,pk):
    subject = ExamInfo.objects.get(pk=pk)
    questions = []
    for q in subject.get_questions():
        questions.append(q)
    paginator=Paginator(questions,1)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        p_questions=paginator.page(page)
    except(EmptyPage,InvalidPage):
        p_questions=paginator.page(paginator.num_pages)

    context={
        "obj":subject,
        "paginator_question":p_questions,
    }

    return render(request,'check_answer_sheet.html',context)


def SaveAns(request):
    ans=request.GET['ans']
    submitAns=ans.split(',')
    user=request.user

    Evaluate.objects.create(user=user,subject=submitAns[0],question=submitAns[1],answer=submitAns[2],mark=0.0)


    return HttpResponse("hello")


def SubmitExam(request):

    return HttpResponse("Exam submitted")