def divide(L,Low,High):
    p=L[High]
    pi=High
    j=-1
    for i in range(0,High):
        if L[i]<=p:
            j+=1
            L[i],L[j]=L[j],L[i]
    j=j+1
    L[j],L[pi]=L[pi],L[j]
    pi=j
    return pi
def quick(L,Low,High):
    if Low<High:
        pi=divide(L,Low,High)
        quick(L,Low,pi-1)
        quick(L,pi+1,High)
    return 
if __name__=="__main__":
    L=list(map(int,input().split()))
    quick(L,0,len(L)-1)
    print("Sorted=",L)


