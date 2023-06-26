
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
def list_snt(arr):
    for i in range(0,len(arr)):
        if checkSoNguyenTo(arr[i]) is True:
            print(f"({i},{arr[i]})", end=" ")
    print()
with open('input4.txt','r+') as file:
    t = int(file.readline())
    for i in range(t):
        n = int(file.readline())
        num = [int(x) for x in file.readline().split()]
        print(f'Test {i + 1}: ')
        if n <= 0:
            print("INVALID")
        else:
            print(f'Tong cac so là: {sum(num)}')
            print(f'Trung binh cong cac so la: {trung_binh(num,n)}')
            print(f'List cac so nguyen to la ')
            list_snt(num)


