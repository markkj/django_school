from rest_framework import serializers
from django.db import IntegrityError
from .models import Student,School

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id','name','address']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','school','first_name','last_name','age',]

    
