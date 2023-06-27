
def chuyenvi(matrix,m,n):
    for i in range(n):
        for j in range(m):
            print(matrix[j][i],end=" ")
        print()


with open('input8.txt','r+') as file:
    while True:
        data = file.readline()
        if data == '':
            break
        num = [int(x) for x in data.split()]
        m = num[0]
        n = num[1]
        matrix = []
        for i in range(abs(m)):
            matrix.append([int(x) for x in file.readline().split()])
            # print(file.readline().split())
        print("Test")
        print(m,n)
        if m > 0 and n > 0:
            for i in range(m):
                for j in range(n):
                    print(matrix[i][j], end= " ")
                print()
        print(n,m)
        print(chuyenvi(matrix,m,n))