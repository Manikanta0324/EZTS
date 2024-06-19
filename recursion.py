def fact(n):
    if n==0 or n==1:
        return n
    else:
        return n*fact(n-1)
if __name__=="main":
    n=int(input("enter the number"))
    print(fact(n))
    for i in range(n):
        print(fact(n),end=" ")
