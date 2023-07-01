import json
from datetime import datetime

from student import Register,Student,Subject,Birth,FullName
from encode import StudentEncoder,RegisterEncoder,SubjectEncoder
def decode_birth(dic):
    if 'day' in dic:
        return Birth(dic['day'],dic['month'],dic['year'])
    else:
        return None
def decode_fullname(dic):
    if 'first' in dic:
        return FullName(dic['first'],dic['mid'],dic['last'])
    else:
        return None
def decode_subject(dic):
    if 'subject_id' in dic:
        return Subject(dic['subject_id'],dic['subject_name'],dic['credit'])
    else:
        return None
def decode_student(dic):
    if 'id' in dic:
        id = dic['id']
        name = decode_fullname(dic['full_name'])
        birth = decode_birth(dic['birth_date'])
        msv = dic['student_id']
        gpa = dic['gpa']
        major = dic['major']
        return Student(id,name,birth,msv,gpa,major)
    else:
        return dic

def print_arr(arr):
    for i in arr:
        print(i)

def creat_student():
    student = []
    with open('STUDENT.JSON','r+',encoding='UTF-8') as inp:
        data = inp.read()
        student = json.loads(data,object_hook=decode_student)
    return student
def creat_subject():
    student = []
    with open('subject.JSON','r+',encoding='UTF-8') as inp:
        data = inp.read()
        student = json.loads(data,object_hook=decode_subject)
    return student

def decode_register(dct):
    if 'register_time' in dct:
        rid = int(dct['id'])
        subject_id = int(dct['subject_id'])
        student_id = dct['student_id']
        mformat = '%d/%m/%Y %H:%M:%S'
        date_time_str = dct['register_time']
        reg_time = datetime.strptime(date_time_str, mformat)
        return Register(rid, student_id, subject_id, reg_time)
    else:
        return dct
def creat_reg(students,sub):
    reg = []
    reg.append(Register(student=students[0],subject=sub[0]))
    reg.append(Register(student=students[1], subject=sub[1]))
    reg.append(Register(student=students[2], subject=sub[2]))
    reg.append(Register(student=students[3], subject=sub[3]))
    reg.append(Register(student=students[4], subject=sub[4]))
    reg.append(Register(student=students[5], subject=sub[5]))
    reg.append(Register(student=students[6], subject=sub[6]))
    reg.append(Register(student=students[7], subject=sub[7]))
    reg.append(Register(student=students[3], subject=sub[1]))
    return reg

def encode_Student(student):
    with open('student_out.json','w+',encoding='UTF-8') as out:
        data = json.dumps(student,ensure_ascii=False,indent=4,cls=StudentEncoder)
        out.write(data)

def encode_Subject(student):
    with open('subject_out.json','w+',encoding='UTF-8') as out:
        data = json.dumps(student,ensure_ascii=False,indent=4,cls=SubjectEncoder)
        out.write(data)
def encode_Register(reg):
    with open('register_out.json','w+',encoding='UTF-8') as out:
        data = json.dumps(reg,ensure_ascii=False,indent=4,cls=RegisterEncoder)
        out.write(data)

students = creat_student()
subject = creat_subject()
register = creat_reg(students,subject)

print_arr(students)
print_arr(subject)
print_arr(register)

encode_Student(students)
encode_Subject(subject)
encode_Register(register)