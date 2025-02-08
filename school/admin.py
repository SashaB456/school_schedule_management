from django.contrib import admin
from school.models import Subject, Student, Class, Teacher
# Register your models here.
admin.register(Subject)
admin.register(Teacher)
admin.register(Class)
admin.register(Student)