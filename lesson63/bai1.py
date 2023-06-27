
def sum(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum
def trung_binh(arr,n):
    summ = sum(arr)
    return summ / n

def checkSoNguyenTo(n):
    if n < 2:
        return False
    for i in range(2,n,1):
        if n % i == 0:
            return False
    return True
def list_snt(arr,out):
    for i in range(0,len(arr)):
        if checkSoNguyenTo(arr[i]) is True:
            out.write(f"({i},{arr[i]}) ")
    out.write('\n')
def count_x(arr,x):
    count = 0
    for i in arr:
        if i == x:
            count += 1
    return count
with open('input5.txt','r+') as file, open('output1.txt','w+',encoding='UTF-8') as out:
    t = int(file.readline())
    for i in range(t):
        num1 = [int(x) for x in file.readline().split()]
        n = num1[0]
        x = num1[1]
        num = [int(x) for x in file.readline().split()]
        out.write(f'Test {i + 1}: \n')
        if n <= 0:
            out.write("INVALID\n")
        else:
            out.write(f'Tong cac so là: {sum(num)}\n')
            out.write(f'Trung binh cong cac so la: {trung_binh(num,n)}\n')
            out.write(f'List cac so nguyen to la \n')
            list_snt(num,out)
            out.write(f'So lan xuat hien cua {x} la: {count_x(num,x)} \n')


