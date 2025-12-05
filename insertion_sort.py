#Insertion Sort



lis1=[645,4367,46,64327,48378,43528,75,1,5,74,3456]
list=[]

for j in range(len(lis1)-1):
    l=None
    for num in lis1:
        if l==None or num<l:
            l=num
        else:
            continue
    lis1.remove(l)
    list.append(l)
print(list)
