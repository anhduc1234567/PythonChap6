class FullName:
    def __init__(self,first,mid,last):
        self.first = first
        self.mid = mid
        self.last = last
    def __str__(self):
        return f'{self.first} {self.mid} {self.last:10}'

class Address:
    def __init__(self, wards, district, city):
        self.wards = wards
        self.district = district
        self.city = city

    def __str__(self):
        return f'{self.wards}, {self.district}, {self.city}'

class Student:
    """This class describe student infomation."""
    def __init__(self, sid, name, age, major, address, gpa):
        self.student_id = sid
        self.full_name = name
        self.age = age
        self.major = major
        self.address = address
        self.gpa = gpa

    def __str__(self):
        return f'Student[id={self.student_id:10}, full_name = {self.full_name}, ' \
               f'age={self.age:5}, major={self.major:5}, address = {self.address},' \
               f' gpa={self.gpa:5}]'
