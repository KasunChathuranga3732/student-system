from django.shortcuts import render
import pandas as pd
import numpy as np
from multiprocessing import Pool
from django.http import HttpResponse
from django.http import JsonResponse


data = pd.DataFrame
data = pd.read_csv('/home/kasun/Documents/assessment/Interview_dataset/Ganison_dataset/Ganison_dataset_5.csv')

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


def assessment_area_list(request):
    global assess_areas
    unique_assessment = data['Assessment Areas'].unique()
    assess_areas = {asses: f"AA{i + 1}" for i, asses in enumerate(unique_assessment)}
    
    return JsonResponse(assess_areas)


def answer_list(request):
    global answers
    unique_answer = data['Answers'].unique()
    answers = {ans: f"Ans{i + 1}" for i, ans in enumerate(sorted(unique_answer))}
    
    return JsonResponse(answers)


def correct_answer_list(request):
    global correct_answers
    unique_correct_answer = data['Correct Answers'].unique()
    newList = sorted(unique_correct_answer.tolist())
    if newList[0] == '?':
        newList.pop(0)
        newList.append('?')
    correct_answers = {cor: f"CorAns{i + 1}" for i, cor in enumerate(newList)}
    
    return JsonResponse(correct_answers)


def category_list(request):
    global categories
    unique_catagory = data['strength_status'].unique()
    categories = {cat: f"CAT{i + 1}" for i, cat in enumerate(sorted(unique_catagory))}
    
    return JsonResponse(categories)


def award_list(request):
    global awards
    unique_award = data['award'].unique()
    awards = {awr: f"AWD{i + 1}" for i, awr in enumerate(unique_award)}
    
    return JsonResponse(awards)


# def subject_list(data):
#     unique_subject = data.drop_duplicates(subset=['Subject'], keep='first')
#     print(unique_subject)
#     subjects = []

#     for i, row in unique_subject.iterrows():
#         subject = [f"Sub{len(subjects) + 1}", row['Subject'], row['average_score']]
#         subjects.append(subject)

#     return subjects


def subject_list(request):
    global subjects
    unique_subject = data['Subject'].unique()
    subjects = {sub: f"Sub{i + 1}" for i, sub in enumerate(unique_subject)}
    
    return JsonResponse(subjects)


def summary_list(request, summaryId):
    result = []
    begin = (summaryId - 1) * 5000
    end = begin + 5000
    dataList = data.iloc[begin:end]
    result = summary_process(dataList)
    
    return JsonResponse(result, safe=False)


def summary_process(dataList):
    results = []
    for index, row in dataList.iterrows():
        school = schools.get(row['school_name'])
        sydney_participants = row['sydney_participants']
        sydney_percentile = row['sydney_percentile']
        assessment_area_id = assess_areas.get(row['Assessment Areas'])
        award_id = awards.get(row['award'])
        class_id = classes.get(row['Class'])
        correct_answer_percentage_per_class = row['correct_answer_percentage_per_class']
        correct_answer = row['Correct Answers']
        student_id = row['StudentID']
        participant = row['participant']
        student_score = row['student_score']
        subject_id = subjects.get(row['Subject'])
        category_id = categories.get(row['strength_status'])
        year_level_name = row['Year Level']
        answer_id = answers.get(row['Answers'])
        correct_answer_id = correct_answers.get(row['Correct Answers'])

        student = [school, sydney_participants, sydney_percentile, assessment_area_id, award_id,
                   class_id, correct_answer_percentage_per_class, correct_answer, student_id, participant,
                   student_score, subject_id, category_id, year_level_name, answer_id, correct_answer_id]
        
        results.append(student)
    
    return results