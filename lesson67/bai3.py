from student import Student,Address,FullName
import xml.etree.ElementTree as et

def parse_xml():
    menu = []
    tree = et.parse('input3.xml')
    root = tree.getroot()
    for i in root:
        id = i[0].text
        age = int(i[1].text)
        major = i[2].text
        gpa = float(i[3].text)
        first = i[4][0].text
        mid = i[4][1].text
        last = i[4][2].text
        wards = i[5][0].text
        dic = i[5][1].text
        city = i[5][2].text
        fullname =FullName(first,mid,last)
        address = Address(wards,dic,city)
        menu.append(Student(id,fullname,age,major,address,gpa))
    return  menu
def print_arr(arr):
    for i in arr:
        print(i)
def write_xml(students):
    root = et.Element('students')
    for stu in students:
        student = et.SubElement(root,'student')
        et.SubElement(student,'id').text = stu.student_id
        et.SubElement(student,'major').text = stu.major
        et.SubElement(student,'gpa').text = str(stu.gpa)
        et.SubElement(student,'age').text = str(stu.age)
        address = et.SubElement(student,'address')
        et.SubElement(address,'wards').text = stu.address.wards
        et.SubElement(address,'district').text = stu.address.district
        et.SubElement(address,'city').text =stu.address.city
        fullname = et.SubElement(student,'fullname')
        et.SubElement(fullname,'first').text = stu.full_name.first
        et.SubElement(fullname, 'mid').text = stu.full_name.mid
        et.SubElement(fullname, 'last').text = stu.full_name.last
    et.indent(root,space='\t')
    return str(et.tostring(root,encoding='UTF-8',xml_declaration=True),'UTF-8')






students = parse_xml()
print_arr(students)
with open('output3.xml','w+',encoding='UTF-8') as out:
    data = write_xml(students)
    out.write(data)