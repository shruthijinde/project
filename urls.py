from django.urls import path

from StudentApp import views

urlpatterns =[
    path('',views.login_fun,name='log'),  #it will redirect to login.html page
    path('reg',views.register_fun,name='reg'),#it will redirect to register.html page and create a account
    path('home',views.home_fun,name='home'),
    path('add_course',views.addcourse_fun,name='add_course'), #rediecting to addcourse.html page and inserting course data into course table
    path('display_course',views.display_course_fun,name='display_course'), #it will collect the data from course table and send to displaycourse
    path('update_course/<int:courseid>',views.updatecourse_fun,name='update_course'), #it will update the course data
    path('delete_course/<int:courseid>',views.deletecourse_fun,name='delete_course'), # it will delete data from the course table
    path('addstudent',views.addstudent_fun,name='addstudent'),  #it will display addstudent.html file and read the data from file and store it in student table
    path('displaystudent',views.displaystudent_fun,name='displaystudent'),  #it will display the entire student data
    path('updatestudent/<int:stud_id>',views.updatestudent_fun,name='updatestudent'),
    path('deletestudent/<int:stud_id>',views.deletestudent_fun,name='deletestudent'),
    path('logout',views.logout_fun,name='logout')
]


