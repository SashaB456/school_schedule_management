from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    subject = models.ManyToManyField(Subject)

    def __str__(self):
        return f"{self.name} ({self.subject.name})"

class Class(models.Model):
    name = models.CharField(max_length=5)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ManyToManyField(Teacher)
    class1 = models.ForeignKey(Class, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.name} - {self.class1.name} (Teacher: {self.teacher.name})"
