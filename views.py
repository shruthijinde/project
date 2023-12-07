from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache

from StudentApp.models import course, City, Student


# Create your views here.
def login_fun(request):
    if request.method == "POST":
        user_name = request.POST['txtUsername']
        user_pswd = request.POST['txtPassword']
        u1 = authenticate(username=user_name,password=user_pswd)  #it will return user object
        if u1 is not None:
             if u1.is_superuser:       #checking wheather it is superuser or not
                request.session['Uname'] = user_name
                login(request,u1)
                return redirect('home')
        else:
            return render(request,'login.html',{'msg':'username and password is incorrect'})
    else:
        return render(request,'login.html')


def register_fun(request):
    if request.method == "POST":  #this code will excecute when we click on submit button in regiister.html page
        user_name = request.POST['txtUserName']
        user_pswd = request.POST['txtPassword']
        user_email = request.POST['txtMail']
        if User.objects.filter(username=user_name).exists():
            return render(request,'register.html',{'msg':'use proper username and password'})
        else:
          u1 = User.objects.create_superuser(username=user_name,password=user_pswd,email=user_email)
          u1.save()
          return redirect('log')
    else:       #this code will execute when we click on hyperlink in login.html page
        return render(request,'register.html')

@login_required
@never_cache
def home_fun(request):
    return render(request,'home.html',{'data':request.session['Uname']})

@login_required
@never_cache
def addcourse_fun(request):
    if request.method == 'POST':
       c1 = course()
       c1.course_name = request.POST['txtCourseName']
       c1.course_duration = request.POST['txtCourseDuration']
       c1.course_fees = request.POST['txtCourseFees']
       c1.save()
       return render(request,'addcourse.html',{'msg':'successfully added'})
    else:
        return render(request,'addcourse.html')

@login_required
@never_cache
def display_course_fun(request):
    course_data = course.objects.all()  #it will return list of objects
    return render(request,'displaycourse.html',{'data':course_data})

@login_required
@never_cache
def updatecourse_fun(request,courseid):
    c1 = course.objects.get(id=courseid)
    if request.method == 'POST':    #when we click on submit if block code will get executed beacause submit
        c1.course_name = request.POST['txtCourseName']
        c1.course_duration = request.POST['txtCourseDuration']
        c1.course_fees = request.POST['txtCourseFees']
        c1.save()
        return redirect('display_course')

    else:  #when we click on hyperlink else block code will get executed
        return render(request,'updatecourse.html',{'data':c1})

@login_required
@never_cache
def deletecourse_fun(request,courseid):
    c1 = course.objects.get(id=courseid)  #get the data based on the courseid which is passed through
    c1.delete()                        #delete the data which is inside the object
    return redirect('display_course')


class Course:
    pass

@login_required
@never_cache
def addstudent_fun(request):
    if request.method == 'POST':
        s1 = Student()
        s1.stud_name = request.POST['txtName']
        s1.stud_phno = request.POST['txtPhno']
        s1.stud_email = request.POST['txtMail']
        s1.stud_city = City.objects.get(city_name=request.POST['ddlCity'])
        s1.stud_course = course.objects.get(course_name=request.POST['ddlCourse'])
        s1.paid_fees = int(request.POST['txtPaidFees'])

        c1 = course.objects.get(course_name=request.POST['ddlCourse'])
        s1.pending_fees = c1.course_fees - s1.paid_fees
        s1.save()
        return redirect('addstudent')
    else:
        city = City.objects.all()
        Course = course.objects.all()
    return render(request,'addstudent.html',{'CityData':city,'CourseData':Course})

@login_required
@never_cache
def displaystudent_fun(request):
    s1 = Student.objects.all()
    return render(request,'displaystudent.html',{'studentdata':s1})

@login_required
@never_cache
def updatestudent_fun(request,stud_id):
    s1 = Student.objects.get(id=stud_id)
    if request.method == 'POST':
        s1.stud_name = request.POST['txtName']
        s1.stud_phno = int(request.POST['txtPhno'])
        s1.stud_email = request.POST['txtMail']
        s1.stud_city = City.objects.get(city_name=request.POST['ddlCity'])
        s1.stud_course = course.objects.get(course_name=request.POST['ddlCourse'])
        s1.paid_fees = s1.paid_fees + int(request.POST['txtPaidFees'])

        c1 = course.objects.get(course_name=request.POST['ddlCourse'])
        if s1.pending_fees > 0:
            s1.pending_fees = s1.pending_fees - s1.paid_fees
        else:
            s1.pending_fees = 0
        s1.save()
        return redirect('displaystudent')
    else:
        city = City.objects.all()
        Course = course.objects.all()
        return render(request,'updatestudent.html',{'student':s1,'CityData':city,'CourseData':Course})

@login_required
@never_cache
def deletestudent_fun(request,stud_id):
    s1 = Student.objects.get(id=stud_id)
    s1.delete()
    return redirect('displaystudent')


def logout_fun(request):
    logout(request)
    return redirect('log')