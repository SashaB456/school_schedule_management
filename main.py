import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "schedule.settings")
django.setup()
from school.models import Student, Class, Teacher, Subject
subject1 = Subject(name="Python")
subject1.save()
teacher1 = Teacher(name = "Maksim", subject = subject1)
teacher1.save()
classpa = Class(name = "PA")
classpa.save()
student = Student(name = "Sasha", teacher = teacher1, class1 = classpa)
student.save()
print(student)