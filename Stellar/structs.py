# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 05:46:05 2017

@author: Uwemuke
"""

from student import Student

students =[]

for i in range(3):
    name = input(str("Your Name: "))
    dorm = input(str("Your Dorm: "))
    
    """print(name, end="")
    
    print(dorm, end="")
    """
    
    students.append(Student(name, dorm))
    
for student in students:
    print(student.name + " is in " + student.dorm)
    