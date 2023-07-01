
class FullName:
    def __init__(self,first,mid,last):
        self.first = first
        self.mid = mid
        self.last = last

    def __str__(self):
        return f'{self.first:8} {self.mid:10} {self.last:10}'

class Person:
    def __init__(self,CCCD,name,birth):
        self.id = CCCD
        self.name = name
        self.birth = birth
    def setFullName(self,name):
        value = name.split()
        mid = ''
        for i in range(1,len(value) -1):
            mid += value[i] + ' '
        self.name = FullName(value[0],mid.strip(), value[len(value) -1])

    def __str__(self):
        return f"{self.id:5} {self.name} {self.birth}"

class Student(Person):
    AUTO = 1000
    def __init__(self, CCCD, name=None, birth='', msv=None, major='', gpa=0.0):
        super().__init__(CCCD, name, birth)
        if msv == None:
            self.msv =f'SV{Student.AUTO}'
            Student.AUTO += 1
        else:
            self.msv = msv
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return f'{super().__str__()} {self.msv:5} {self.major:5} {self.gpa}'


class Course:
    AUTO_ID = 100
    def __init__(self,id = None,name = '', subject =None,teacher =None,room =''):
        if id == None:
            self.id = Course.AUTO_ID
            Course.AUTO_ID += 1
        else:
            self.id = id
        self.subject = subject
        self.teacher =teacher
        self.room = room
        self.transcripts = []
        self.name = name

    def __str__(self):
        return f'{self.id:10}{self.name:20}{self.subject.ids:<10}' \
               f'{self.subject.name:30}{self.teacher.idt:10}' \
               f'{self.teacher.name}{self.room:10}'

class Teacher(Person):
    AUTO =1000
    def __init__(self, salary, CCCD='', name='', birth='', idt=None, exp=''):
        super().__init__(CCCD, name, birth)
        if idt is None:
            self.idt = f'GV{Teacher.AUTO}'
            Teacher.AUTO += 1
        else:
            self.idt = idt
        self.exp = exp
        self.salary = salary
    def __str__(self):
        return f'{super().__str__()} {self.idt} {self.exp} {self.salary}'


class Subject:
    auto =1000
    def __init__(self,name,ids = None,credit = 0):
        if id is None:
            self.ids = Subject.auto
            Subject.auto += 1
        else:
            self.ids = ids
        self.name = name
        self.credit = credit
    def __str__(self):
        return f'{self.ids} {self.name} {self.credit}'

class Transcript:
    AUTO = 100
    def __init__(self, tran_id= None, course_id='', student=None, gpa=0.0, capacity=''):
        if tran_id is None:
            self.transcript_id = Transcript.AUTO
            Transcript.AUTO += 1
        else:
            self.transcript_id = tran_id
        self.course_id = course_id
        self.student = student
        self.gpa = gpa
        self.capacity = capacity

    def calculate_capacity(self):
        if 3.6 <= self.gpa <= 4.0:
            self.capacity = 'Xuất sắc'
        elif self.gpa >= 3.2:
            self.capacity = 'Giỏi'
        elif self.gpa >= 2.6:
            self.capacity = 'Khá'
        elif self.gpa >= 2.0:
            self.capacity = 'Trung bình'
        else:
            self.capacity = 'Yếu'

    def __str__(self):
        return f'{self.transcript_id:<10}{self.student.msv:10}' \
               f'{self.student.name} {self.gpa:<10}{self.capacity:15}'