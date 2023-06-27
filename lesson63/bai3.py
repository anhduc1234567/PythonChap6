def read_matrix(num,m,n):
    matrix = []
    for i in range(m):
        matrix.append([])
        for j in range(n):
            matrix[i].append(num[i * n + j])
    return  matrix

with open('input7.txt',"r+") as file, open('output4.txt','w+') as out:
    while True :
        data = file.readline()
        if data == '':
            break
        str1 =[int(x) for x in data.split()]
        m = str1[0]
        n = str1[1]
        if m > 0 and n > 0:
            num = [int(x) for x in file.readline().split()]
            matrix = read_matrix(num,m,n)
            out.write(f'{m} {n}\n')
            for i in range(m):
                for j in range(n):
                    out.write(f'{matrix[i][j]} ')
                out.write('\n')


