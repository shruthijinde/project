from django.db import models

# Create your models here.
class course(models.Model):
    course_name = models.CharField(max_length=100)
    course_duration = models.CharField(max_length=100)
    course_fees = models.IntegerField()

    def __str__(self):
        return self.course_name

class City(models.Model):
    city_name = models.CharField(max_length=150)

    def __str__(self):
        return self.city_name

class Student(models.Model):
    stud_name = models.CharField(max_length=150)
    stud_phno = models.BigIntegerField()
    stud_email = models.CharField(max_length=150)
    paid_fees = models.IntegerField()
    pending_fees = models.IntegerField()
    stud_course  = models.ForeignKey(course,on_delete=models.CASCADE)
    stud_city = models.ForeignKey(City,on_delete=models.CASCADE)