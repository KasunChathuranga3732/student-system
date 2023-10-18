from django.shortcuts import render
import pandas as pd
import numpy as np
from multiprocessing import Pool
from django.http import HttpResponse
from django.http import JsonResponse


data = pd.DataFrame
data = pd.read_csv('/home/kasun/Documents/assessment/Interview_dataset/Ganison_dataset/Ganison_dataset_1.csv')

schools:dict
classes:dict
assess_areas:dict
answers:dict
correct_answers:dict
categories:dict
awards:dict
subjects:dict

def read_csv(request):
    global data
    data = pd.read_csv('/home/kasun/Documents/assessment/Interview_dataset/Ganison_dataset/Ganison_dataset_2.csv')

    # print(len(data))

    response = HttpResponse(status=201)
    return response


def school_list(request):
    global schools
    unique_school = data['school_name'].unique()
    schools = {school: f"SC{i + 1}" for i, school in enumerate(unique_school)}
    
    return JsonResponse(schools)


def student_list(request):
    unique_student = data.drop_duplicates(subset=['StudentID'], keep='first')
    students = unique_student.set_index('StudentID').apply(lambda row: row['First Name'] + ' ' + row['Last Name'], axis=1).to_dict()
    
    return JsonResponse(students)


def class_list(request):
    global classes
    unique_class = data['Class'].unique()
    sorted_class_names = sorted(unique_class, key=extract_number)
    classes = {cls: f"C{i + 1}" for i, cls in enumerate(sorted_class_names)}
    
    return JsonResponse(classes)

def extract_number(class_name):
    return int(class_name.split()[1])

