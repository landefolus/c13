def add_num(listA,num):
    sum=[]
    for i in listA:
        sum.append(i*num)
    return sum

listA = [2, 4, 6, 8]
num=10
result=add_num(listA,num)
print(result)
