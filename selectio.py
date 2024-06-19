l=[9,7,5,10,26,44,3,1]
min=l[0]
for j in range(0,len(l)):
    pos=jmin=l[j]
    for i in range(j,len(l)):
        if l[i]<min:
            min=l[i]
            pos=i
    l[j],l[pos]=l[pos],l[j]
