# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 10:16:01 2017

@author: Uwemuke
"""

from student import Student
import csv

students =[]

for i in range(3):
    name = input(str("Your Name: "))
    dorm = input(str("Your Dorm: "))
    
    students.append(Student(name, dorm))
    
file = open("students.csv", "w")
writer = csv.writer(file)
for student in students:
    writer.writerow((student.name, student.dorm))
file.close()