from math import sqrt
def prime(n):
    f=[]
    n=int(sqrt(n))
    for i in range(n):
        if i>1:
            if n%i==0:
                f.append(i)
                n/=i
                i=2
        if n==1:
            break
    return f

x=input("Potatos: \n")
print prime(x)
