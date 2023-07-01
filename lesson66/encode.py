
import json
from datetime import datetime
from student import Register

class StudentEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__

class SubjectEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__

class RegisterEncoder(json.JSONEncoder):
    def default(self, obj):
        dt = datetime.strftime(obj.time, '%d/%m/%Y %H:%M:%S')
        return {"id": obj.id,
                "student": {
                    "student_id": obj.student.id,
                    "student_name": obj.student.name.first
                },
                "subject":{
                  "subject_id": obj.subject.id,
                    "subject_name": obj.subject.name
                },
                "register_time": dt
                }



