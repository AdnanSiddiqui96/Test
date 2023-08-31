from django.db import models

# Create your models here.

class Class(models.Model):

    class_name = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.class_name


class student(models.Model):

    fisrtname = models.CharField(max_length=255, default='')
    lastname = models.CharField(max_length=255, default='')
    email = models.EmailField(max_length=255, default='')
    contact_number = models.CharField(max_length=255, default='')
    address = models.TextField(default='')
    classid = models.ForeignKey(Class, on_delete =models.CASCADE,blank=True, null=True,related_name="student_class")

    def __str__(self):
        return self.fisrtname + ' ' + self.lastname