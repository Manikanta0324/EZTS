l=[5,3,1,2,4,6,8,12,34]
for i in range(0,len(l)):
    for j in range(0,len(l)-1):
        if l[i]<l[j]:
            min=l[i]
            l[i],l[i+1]=l[i+1],l[i]
print(l)