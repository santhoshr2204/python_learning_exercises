#selection sort


lis1=[645,4367,46,64327,5,74,3456]

list=[]
for j in range(len(lis1)-1):
    l=None
    for i in range(j,(len(lis1)-1)):
        
        if l==None or lis1[i]<l:
            l=lis1[i]
        else:
            continue
    
    swap=lis1[lis1.index(l)]
    lis1[lis1.index(l)]=lis1[j]
    lis1[j]=swap
print(lis1)
    


