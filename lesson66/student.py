import datetime


class FullName:
    def __init__(self,first,mid,last):
        self.first = first
        self.mid = mid
        self.last = last
    def __str__(self):
        return f'{self.first} {self.mid} {self.last:10}'

class Birth:
    def __init__(self,day,month,year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f'{self.day}/{self.month}/{self.year}'

class Student:
    AUTO_ID = 1000
    def __init__(self,id = 0,name = '',birth = '',msv = None,gpa = 0,major = ''):
        self.id = id
        self.name = name
        self.birth = birth
        self.gpa = gpa
        self.major = major
        if msv == None:
            self.msv = f"SV{Student.AUTO_ID}"
            Student.AUTO_ID += 1
        else:
            self.msv = msv
    def __str__(self):
        return f'{self.id} {self.msv} {self.name} {self.birth} {self.major} {self.gpa}'

class Subject:
    AUTO_ID = 1000
    def __init__(self,id = None,name = '',credit = 0):
        self.name = name
        self.credit = credit
        if id is None:
            self.id = Subject.AUTO_ID
            Subject.AUTO_ID += 1
        else:
            self.id = id
    def __str__(self):
        return f'{self.id} {self.name} {self.credit}'

class Register:
    AUTO_ID = 100
    def __init__(self,id =None ,student = None, subject = None,time =None):
        if id == None:
             self.id = Register.AUTO_ID
             Register.AUTO_ID += 1
        else:
            self.id = id
        self.student = student
        self.subject = subject
        if time == None:
            self.time = datetime.datetime.now()
        else:
            self.time = time

    def __str__(self):
        date_str = f'{self.time.day:02}/{self.time.month:02}/' \
                   f'{self.time.year:4} {self.time.hour:02}:' \
                   f'{self.time.minute:02}:{self.time.second:02}'
        return f'{self.id:<10}{self.student.id:10} {self.student.name}' \
               f'{self.subject.id:10} {self.subject.name}' \
               f'{date_str:25}'

