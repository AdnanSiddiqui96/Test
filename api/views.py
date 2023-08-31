from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response

# Create your views here.

class index(APIView):

    def get(self,request):

        return HttpResponse("ok")

    def post(self,request):

        return HttpResponse("ok")

    def put(self,request):

        return HttpResponse("ok")

    def delete(self,request):

        return HttpResponse("ok")


class Student(APIView):

    def get(self,request):

        data = student.objects.values()
        return Response({'status':True,'data':data})

    def post(self,request):

        fisrtname = request.data.get('fisrtname')
        lastname = request.data.get('lastname')
        # lastname = request.data['lastname']
        email = request.data.get('email')
        contact_number = request.data.get('contact_number')
        address = request.data.get('address')
        class_id = request.data.get('class_id')

        classObj = Class.objects.filter(id  = class_id).first()
        

        data = student(fisrtname = fisrtname,lastname=lastname,email=email,contact_number=contact_number,address=address,classid = classObj)

        data.save()

        return Response({'status':True,'message':"Add successfully"})
    

    def delete(self,request):

        id = request.GET['id']
        
        data = student.objects.filter(id = id)
        data.delete()

        return Response({'status':True,'message':"delete successfully"})


    def put(self,request):

      
        id = request.data.get('id')
        fisrtname = request.data.get('fisrtname')
        lastname = request.data.get('lastname')
        # lastname = request.data['lastname']
        email = request.data.get('email')
        contact_number = request.data.get('contact_number')
        address = request.data.get('address')
        
        data = student.objects.filter(id = id).first()
        data.fisrtname = fisrtname
        data.lastname = lastname
        data.email = email
        data.contact_number = contact_number
        data.address = address
        data.save()

        return Response({'status':True,'message':"updated successfully"})


class GetStudent(APIView):

    def get(self, request):

        classid = request.GET.get('classid')  

        data = student.objects.filter(classid =classid).values() 
        return Response({'status':True,'data':data})



class GetStudents(APIView):

    def get(self, request):

        classid = request.GET.get('classid')  

        data = Class.objects.get(id = classid).student_class.all().values() 
        return Response({'status':True,'data':data})