from .views import *
from django.urls import path
urlpatterns = [


    path('index',index.as_view()),
    path('Student',Student.as_view()),
    path('GetStudent',GetStudent.as_view()),
    path('GetStudents',GetStudents.as_view()),
    




]