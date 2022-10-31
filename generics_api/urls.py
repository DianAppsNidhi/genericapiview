from django.contrib import admin
from django.urls import path
from .views import CourseListCreateView, CourseDetailView


urlpatterns = [
    path('courses', CourseListCreateView.as_view()),
    path('courses/<int:pk>', CourseDetailView.as_view())
]