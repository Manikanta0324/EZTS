l=[3,5,2,14,-1,7,7,9,-1,5,5,-1,-1]
n=[0]*len(l)
for i in range(0,len(l)):
    for j in range(i,len(l)):
        if l[i]<l[j]:
            n[i]=l[j]
            i=i+1
            break
        if l[i]>=l[j]:
            n[i]=-1
print(n)
