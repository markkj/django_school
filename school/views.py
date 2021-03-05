from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status , filters
from .models import Student,School
from .serializers import SchoolSerializer, StudentSerializer



class SchoolViewSet(viewsets.ModelViewSet):
    """
        for viewing and editing School
    """
    queryset  = School.objects.all()
    serializer_class = SchoolSerializer
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    

class StudentViewSet(viewsets.ModelViewSet):
    """
        for viewing and editing Student
    """
    queryset  = Student.objects.all()
    serializer_class = StudentSerializer
    search_fields = ['first_name']
    filter_backends = (filters.SearchFilter,)

    def create(self, request, *args,**kwargs):
        school = School.objects.get(id=request.data['school']) 
        if Student.objects.filter(school=school.id).count() >= school.maximum_student:
            return Response({"errors":"This school is already full of students."}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer_class = StudentSerializer(data=request.data) 
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)