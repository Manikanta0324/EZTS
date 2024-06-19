def merge(l,low,mid,high):
    left=l[low:mid]
    right=l[mid:high+1]
    i=j=t=0
    temp=[0]*len(l)
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            temp[t]=left[i]
            i+=1
            t+=1
        else:
            temp[t]=right[j]
            j+=1
            t+=1
    while i<len(left):
        temp[t]=left[i]
        i+=1
        t+=1
    while j<len(right):
        temp[t]=right[j]
        j+=1
        t+=1
def merge(l,low,high):
    if low<high:
        mid=low+(high-low)//2
        merge(l,low,mid)
        merge(l,mid+1,high,temp)
        merge(l,low,mid,high,temp)
    return
if __name__=="__main__"



 