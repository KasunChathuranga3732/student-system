"""SchoolProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from SchoolApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('read/', views.read_csv, name='csv_data'),
    path('schools/', views.school_list, name='Schools'),
    path('classes/', views.class_list, name='Classes'),
    path('students/', views.student_list, name='Students'),
    path('assess-areas/', views.assessment_area_list, name='Assess'),
    path('answers/', views.answer_list, name='Answers'),
    path('cor-answers/', views.correct_answer_list, name='CAnswers'),
    path('categories/', views.category_list, name='Categories'),
    path('awards/', views.award_list, name='Awards'),
    path('subjects/', views.subject_list, name='Subjects'),
    path('summary/', views.summary_list, name='Summary'),
]
