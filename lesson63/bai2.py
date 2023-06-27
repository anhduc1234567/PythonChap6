with open('input6.txt','r+') as file,open('output2.txt','w+',encoding='UTF-8') as out:
    n = int(file.readline())
    for i in range(n):
        str = [x for x in file.readline().split()]
        str.sort(reverse=True)
        out.write(f"Test: {i} \n")
        for i in str:
            out.write(f'{i} ')
        out.write('\n')
