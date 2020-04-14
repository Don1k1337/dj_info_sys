from django.shortcuts import render
from django.views.generic import ListView
from .models import *
from .models import StudentProgram
#View of existing models

class CourseListView(ListView):
    model = Course

class StudentListView(ListView):
    model = StudentProgram