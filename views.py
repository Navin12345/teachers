from django.shortcuts import render
from rest_framework.views import APIView
from classcast.teachers.models import teacher_info
from classcast.teachers.serializers import teacherserializer
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview

######################

class StudentRequest(APIView):

    def get(self, request, subject, goal):
        if not goal:
                teacher1 = teacher_info.filter(subject = subject)
                serializer = teacherserializer(teacher1, many = True)
                return Response(serializer.data)
        teacher2 = teacher_info.filter(subject = subject, goal = goal)
        serializer = teacherserializer(teacher2, many = True)
        return Response(serializer.data)