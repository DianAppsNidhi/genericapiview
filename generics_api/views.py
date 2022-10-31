from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Course, CourseSerializer
from rest_framework import mixins, generics
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# class CourseListCreateView(generics.ListAPIView, generics.CreateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer





# class CourseDetailView(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer




class CourseListCreateView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer    


class CourseDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer   