 #1,2,0,1,0,4,0
#Output:
 #1,2,1,4,0,0,0'''
def moveZero(arr,n):
    temp=[]
    for i in range(n):
        if arr[i]!=0:
            temp.append(arr[i])
    nz=len(temp)
    for i in range(nz):
        arr[i]=temp[i]
    for i in range(nz,n):
        arr[i]=0
    return arr
n=int(input())
arr=list(map(int,input().split()))
res=moveZero(arr,n)
for i in res:
    print(i,end=' ')
print()


