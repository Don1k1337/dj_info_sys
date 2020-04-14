from django.urls import path
from .views import CourseListView, StudentListView

urlpatterns = [
path('course/', CourseListView.as_view()),
path('student/', StudentListView.as_view()),
path('uni/', home_view, name='home')

]