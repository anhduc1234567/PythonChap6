import datetime


class Person:
    def __init__(self,id,name,birth):
        self.id = id
        self.name = name
        self.birth = birth
    def __str__(self):
        return f'ID: {self.id} Name: {self.name}   '\
                f'Birth: {self.birth}'
class Student(Person):
    ID_AUTO = 1000
    def __init__(self,gpa,major, id, name, birth):
        super().__init__(id,name,birth)
        self.msv = f'SV{Student.ID_AUTO}'
        self.gpa = gpa
        self.major = major
        Student.ID_AUTO += 1
    def __str__(self):
        return f'{super().__str__()} MSV: {self.msv} '\
                f'{self.major} Gpa: {self.gpa}'
class Subject:
    ID_AUTO = 1000
    def __init__(self,name,sotin):
        self.id = Subject.ID_AUTO
        self.name = name
        self.sotin = sotin
        Subject.ID_AUTO += 1
    def __str__(self):
        return f'{self.id} {self.name} {self.sotin}'

class Register:
    AUTO_ID = 1000
    def __init__(self,subject,student):
        self.id = Register.AUTO_ID
        self.subject = subject
        self.student = student
        Register.AUTO_ID += 1
        self.time = datetime.datetime.now()

    def __str__(self):
        date_str = f'{self.time.day:02}/{self.time.month:02}/' \
                   f'{self.time.year:4} {self.time.hour:02}:' \
                   f'{self.time.minute:02}:{self.time.second:02}'
        return f'{date_str} {self.id} {self.subject.name} {self.student.name}'

def creat_student():
    students = []
    with open("student.dat",'r+',encoding="UTF-8") as inp:
        while True:
            cccd = inp.readline().strip()
            if cccd == '':
                break
            name = inp.readline().strip()
            birth = inp.readline().strip()
            gpa = float((inp.readline()).strip())
            major = inp.readline().strip()
            students.append(Student(gpa,major,cccd,name,birth))
    return students
def creat_subject():
    subject = []
    with open('subject.dat','r+') as inp:
        while True:
            name = inp.readline().strip()
            if name == '':
                break
            sotin = int(inp.readline().strip())
            subject.append(Subject(name,sotin))
    return subject
def print_arr(arr):
    for i in arr:
        print(i)

students = creat_student()
subject = creat_subject()
print_arr(students)
print()
print_arr(subject)