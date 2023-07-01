import json
from collections import OrderedDict
from operator import itemgetter


class Birth:
    def __init__(self,day,month,year):
        self.day = day
        self.month = month
        self.year = year
    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"
class Student:
    def __init__(self,id,name,birth,gpa):
        self.id = id
        self.name = name
        self.birth = birth
        self.gpa = gpa
    def __str__(self):
        return f'{self.id} {self.name} {self.birth} {self.gpa}'

def decode_birth(dic):
    if 'day' in dic:
        return Birth(dic['day'],dic['month'],dic['year'])
    else:
        return None

def decode_student(dct):
    if 'birth_date' in dct:
        birth_date = decode_birth(dct['birth_date'])
        return Student(dct['id'], dct['name'], birth_date, float(dct['gpa']))
    else:
        return dct
def print_arr(arr):
    for i in arr:
        print(i)
def list_by_gpa(arr):
    result = {}
    for i in arr:
        if i.gpa in result:
            result[i.gpa] += 1
        else:
            result[i.gpa] = 1
    for i in result.keys():
        print(f'{i}: {result[i]}')
def list_by_month(arr):
    result = {}
    #arr.sort(key=lambda x: (x.birth.month))
    for i in arr:
        if i.birth.month in result:
            result[i.birth.month] += 1
        else:
            result[i.birth.month] = 1
    result = OrderedDict(sorted(result.items(), key=itemgetter(1)))
    '''Xắp xếp theo value'''
    for i in result.keys():
        print(f'{i}: {result[i]}')

with open('input3.json','r+',encoding='UTF-8') as inp3:
    data = inp3.read()
    students = json.loads(data,object_hook=decode_student)
    print("----DANH SACH SINH VIEN ---")
    print_arr(students)
    print("---SAP SEP THEO DTB GIAM DAN TEN TANG DAN")
    students.sort(key = lambda x:(-x.gpa,x.name))
    print_arr(students)
    print("--DANH SACH THEP GPA")
    list_by_gpa(students)
    print("--DANH SACH THEO THANG--")
    list_by_month(students)
