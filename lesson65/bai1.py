import json
from collections import OrderedDict
from operator import itemgetter


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'{self.name} {self.age}'
class Subject:
    def __init__(self,subject_id,name,credit,leson):
        self.subject_id = subject_id
        self.subject_name = name
        self.credit = credit
        self.lesson = leson

    def __str__(self):
        return f'{self.subject_id} {self.subject_name} '\
                f'{self.credit} {self.lesson}'
def decode_subject(dic):
    if 'subject_id' in dic:
        id = dic['subject_id']
        name = dic['subject_name']
        credit = dic['subject_credit']
        les = dic['subject_lesson']
        return Subject(id,name,credit,les)
    else:
        return None
def decode_person(dic):
    if 'name' in dic:
        name = dic['name']
        age = dic['age']
        return Person(name,age)
    else:
        return None
def print_arr(arr):
    for i in arr:
        print(i)
def list_person_by_age(arr):
    result = {}
    for i in arr:
        if i.age in result:
            result[i.age] += 1
        else:
            result[i.age] = 1
    result = OrderedDict(sorted(result.items(), key=itemgetter(1), reverse=True))
    print('==> Các đối tượng theo từng độ tuổi: ')
    for key in result.keys():
        print(f'{key}: {result[key]}')


with open('input1.json','r+') as inp:
    data = inp.read()
    sub = json.loads(data,object_hook=decode_subject)
    print(sub)
with open('input2.json','r+') as inp2:
    data2 = inp2.read()
    person = json.loads(data2,object_hook=decode_person)
    print_arr(person)
    list_person_by_age(person)
