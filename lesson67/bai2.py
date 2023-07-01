import xml.etree.ElementTree as et
class Catalog:
    def __init__(self,title,artist,country,company,price,year):
        self.title = title
        self.artist = artist
        self.country = country
        self.company =company
        self.price = price
        self.year = year
    def __str__(self):
        return f'{self.title:25} {self.artist:20} {self.country:5} {self.company:15}' \
                f'{self.price:5} {self.year}'

def parse_xml():
    tree = et.parse('input2.xml')
    root = tree.getroot()
    menu = []
    for i in root:
        title = i[0].text
        artist = i[1].text
        country = i[2].text
        compa = i[3].text
        price = i[4].text
        year = int(i[5].text)
        menu.append(Catalog(title,artist,country,compa,price,year))
    return menu
def print_arr(i):

    for j in i:
        print(j)
menu = parse_xml()
print_arr(menu)
