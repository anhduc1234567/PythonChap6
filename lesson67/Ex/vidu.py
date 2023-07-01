import xml.etree.ElementTree as et
class Breakfast:
    def __init__(self,name,price,discription,calo):
        self.name = name
        self.price = price
        self.discription = discription
        self.calo = calo
    def __str__(self):
        return f'{self.name} {self.price} {self.discription} {self.calo}'
def read_xml():
    menu = []
    tree = et.parse('sx.xml')

    root = tree.getroot()
    for i in root:
        name = i[0].text
        price = i[1].text
        dis = i[2].text
        calo = i[3].text
        menu.append(Breakfast(name,price,dis,calo))
    return menu
def print_arr(arr):
    for i in arr:
        print(i)
menu = read_xml()
menu.sort(key=lambda x:(x.price))
print_arr(menu)