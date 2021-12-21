from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
# from django.http import HttpResponse,JsonResponse
# Create your views here.
@api_view(['GET'])
def apioverview(request):
    api_urls ={
        'university':'/university',
        'university-details':'/university/<int:id>',
        'students':'/students',
        'students-details':'/students/<int:id>',
    }
    return Response(api_urls)

class UniversityList(APIView):
    def get(self, request, format=None):
        university = University.objects.all()
        serializer = UniversitySerializer(university,many=True)
        return Response(serializer.data, status=200)
    def post(self,request):
        data = request.data
        serializer =UniversitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)    

class UniversityDetail(APIView):
    def get_object(self,id):
        try:
            return University.objects.get(id=id)
        except University.DoesNotExist:
            raise Http404    
    def get(self,request,id):
        university = self.get_object(id)
        serializer = UniversitySerializer(university)
        return Response(serializer.data)  
    def put(self,request,id=None):  
        data = request.data
        university = University.objects.get(id=id)
        serializer =UniversitySerializer(university,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)          

class StudentsList(APIView):
    def get(self, request, format=None):
        student = Students.objects.all()
        serializer = StudentsSerializer(student,many=True)
        return Response(serializer.data, status=200)
    def post(self,request):
        data = request.data
        serializer =StudentsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400) 

class StudentsDetail(APIView):
    def get_object(self,id):
        try:
            return Students.objects.get(id=id)
        except Students.DoesNotExist:
            raise Http404    
    def get(self,request,id=None):
        students = self.get_object(id)
        serializer = StudentsSerializer(students)
        print(serializer,'oooooooooo')
        return Response(serializer.data)  
    def put(self,request,id=None):  
        data = request.data
        students = Students.objects.get(id=id)
        serializer =StudentsSerializer(students,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400) 
    def delete(self, request, id, format=None):
        students = self.get_object(id)
        students.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    





