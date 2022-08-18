from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.

def account(request):
    return render(request,'home_base.html')
def test(request):
    return render(request,'test2.html')

def Teacher_signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        designation = request.POST['designation']
        teacher_id = request.POST['teacher_id']
        email = request.POST['email']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        check_user=User.objects.filter(username=username)
        teacher_obj = Teacher.objects.filter(teacher_id=teacher_id)
        l_t_id = len(teacher_obj)
        l_user = len(check_user)
        try:
            if l_user == 0:
                if l_t_id != 0:

                    if password1 == password2:
                        User.objects.create_user(username=username,email=email,password=password1,is_teacher=True)
                        data = Teacher()
                        data.designation = designation
                        data.teacher_id = teacher_id
                        data.phone = phone
                        data.save()
                        user = authenticate(username=username, password=password1)
                        login(request, user)

                        return HttpResponseRedirect('/account/')
                    else:
                        messages.warning(request, 'password does not match')
                        print("pass does not match")
                else:
                    messages.warning(request,'invalid teacher id')
                    print("invalid teacher id")
            else:
                messages.warning(request, 'username already taken')
                print("user name already teaken")
        except:
            messages.warning(request,'username already taken')
            print("username already taken")



    return render(request,'teacher_signup.html')



def Student_signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        s_name = request.POST['s_name']
        student_id = request.POST['student_id']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        check_user=User.objects.filter(username=username)
        student_obj = Student.objects.filter(student_id=student_id)
        l_t_id = len(student_obj)
        l_user = len(check_user)

        if l_user == 0:
            if l_t_id != 0:

                if password1 == password2:
                    User.objects.create_user(username=username,email=email,password=password1,is_student=True)
                    user = authenticate(username=username, password=password1)
                    login(request, user)
                    data = Student()
                    data.user = request.user
                    data.name = s_name
                    data.student_id = student_id
                    data.save()

                    return HttpResponseRedirect('/account/')
                else:
                    messages.warning(request, 'password does not match')
                    print("pass does not match")
            else:
                messages.warning(request,'invalid student id')
                print("invalid student id")
        else:
            messages.warning(request, 'username already taken')
            print("user name already teaken")




    return render(request,'student_signup.html')



def Login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password = request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            #current_user=request.user
            #userprofile=UserProfile.objects.get(user_id=current_user.id)
            #request.session['userimage']=userprofile.image.url
            return HttpResponseRedirect('/account/')
        else:
            messages.warning(request,'invalid username or password')
            return HttpResponseRedirect('/login/')
    return render(request,'login.html')


def Logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

