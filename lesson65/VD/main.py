import json
from student import FullName,Address,Student
def decode_fullname(name):
    if 'first' in name:
        return FullName(name['first'],name['mid'],name['last'])
    else:
        return None
def decode_address(address):
    if 'wards' in address:
        return Address(address['wards'],address['district'],address['city'])
    else:
        return None
def decode_student(dtc):
    if 'id' in dtc:
        id = dtc['id']
        age = dtc['age']
        major = dtc['major']
        gpa = dtc['gpa']
        fullname = decode_fullname(dtc['full_name'])
        address = decode_address(dtc['address'])
        return Student(id, fullname, age, major, address, gpa)
    else:
        return dtc
class StudentEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__
def print_arr(arr):
    for i in arr:
        print(i)
def list_by_district(arr:list):
    result = {}
    for i in arr:
        if i.address.district in result:
            result[i.address.district] += 1
        else:
            result[i.address.district] = 1
    for i in result.keys():
        print(f'{i} - {result[i]}')
with open('input.json','r+',encoding='UTF-8') as inp,\
        open('output.json','w+',encoding='UTF-8') as out:
    data = inp.read()
    students = json.loads(data,object_hook=decode_student)
    print_arr(students)
    print("--------------")
    list_by_district(students)
    dataout = json.dumps(students,cls=StudentEncoder,indent=4,ensure_ascii=False)
    out.write(dataout)