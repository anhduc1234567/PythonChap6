import xml.etree.ElementTree as et
from student import Student,Transcript,Teacher,Subject,Person,Course,FullName

def parse_xml_Student():
    student = []
    tree = et.parse('student.xml')
    root = tree.getroot()
    for i in root:
        id = i[0].text
        first = i[1][0].text
        mid = i[1][1].text
        last = i[1][2].text
        birth = i[2].text
        msv =i[3].text
        gpa = float(i[4].text)
        major = i[5].text
        fullname = FullName(first,mid,last)
        student.append(Student(id,fullname,birth,msv,major,gpa))
    return student
def parse_xml_Teacher():
    student = []
    tree = et.parse('teacher.xml')
    root = tree.getroot()
    for i in root:
        id = i[0].text
        first = i[1][0].text
        mid = i[1][1].text
        last = i[1][2].text
        birth = i[2].text
        id_teache =i[3].text
        salary = int(i[4].text)
        major = i[5].text
        fullname = FullName(first,mid,last)
        student.append(Teacher(salary,id,fullname,birth,id_teache,major))
    return student
def parase_subject():
    sub = []
    tree =et.parse('subject.xml')
    root = tree.getroot()
    for i in root:
        id = i[0].text
        name = i[1].text
        cre = i[2].text
        sub.append(Subject(name,id,cre))
    return sub
def find_subject_by_id(subj,id):
    for i in subj:
        if i.ids == id:
            return i
def find_teacher_by_id(teachers,id):
    for i in teachers:
        if i.idt == id:
            return i
def find_student_by_id(students,id):
    for i in students:
        if i.msv == id:
            return i
def parse_xml_course():
    courses = []
    tree = et.parse('course.xml')
    root = tree.getroot()
    for i in root:
        id = i[0].text
        name = i[1].text
        subject = i[2].text
        teacher = i[3].text
        room = i[4].text
        course = Course(id,name,subject,teacher,room)
        courses.append(course)
    for c in courses:
        c.subject = find_subject_by_id(subjects, c.subject)
        c.teacher = find_teacher_by_id(teachers, c.teacher)
    return courses

def parse_tran():
    tran = []
    tree = et.parse('transcript.xml')
    root = tree.getroot()
    for i in root:
        tranid= i[0].text
        idc= i[1].text
        ids = i[2].text
        gpa = float(i[3].text)
        capacity = i[4].text
        trans = Transcript(tranid,idc,ids,gpa,capacity)
        tran.append(trans)
    for i in tran:
        i.student = find_student_by_id(students,i.student)
    return tran

def write_student(students):
    root = et.Element('students')
    for i in students:
        stu = et.SubElement(root,'student')
        et.SubElement(stu,'person_id').text = i.id
        full_name = et.SubElement(stu,'full_name')
        et.SubElement(full_name,'first').text = i.name.first
        et.SubElement(full_name, 'mid').text = i.name.mid
        et.SubElement(full_name, 'last').text = i.name.last
        et.SubElement(stu,'birth').text = i.birth
        et.SubElement(stu,'student_id').text = i.msv
        et.SubElement(stu,'gpa').text = str(i.gpa)
        et.SubElement(stu,'major').text = i.major
    et.indent(root,space='\t')
    data = str(et.tostring(root,encoding='UTF-8',xml_declaration=True),'UTF-8')
    with open('out_student.xml','w+',encoding='UTF-8') as out:
        out.write(data)
def write_course(courses):
    root = et.Element('courses')
    for c in courses:
        course = et.SubElement(root,'course')
        et.SubElement(course,'course_id').text = str(c.id)
        et.SubElement(course,'teacher_id').text = str(c.teacher.idt)
        et.SubElement(course,'room').text = c.room
        et.SubElement(course,'name').text = c.name
        et.SubElement(course,'subject_id').text = c.subject.ids
    et.indent(root,space='\t')
    data = str(et.tostring(root,encoding='UTF-8',xml_declaration=True),'UTF-8')
    with open('out_course.xml','w+',encoding='UTF_8') as out:
        out.write(data)
def print_arr(arr):
    for i in arr:
        print(i)
students = parse_xml_Student()
teachers = parse_xml_Teacher()
subjects = parase_subject()
courses = parse_xml_course()
transcripts = parse_tran()

print_arr(students)
print_arr(teachers)
print_arr(subjects)
print_arr(courses)
print_arr(transcripts)

write_student(students)
write_course(courses)