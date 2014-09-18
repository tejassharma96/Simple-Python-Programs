print 'Enter 3 numbers'
a=input()
b=input()
c=input()
x=a
y=b
z=c

if(x==y) or (y==z) or (x==z):
    if(x==z) and (y==z) and (x==z):
        print str(x)+"="+str(z)+"="+str(y)
    elif(x==y):
        if(z<x):
            print "("+str(x)+"="+str(y)+")>"+str(z)
        else:
            print "("+str(x)+"="+str(y)+")<"+str(z)
    elif(y==z):
        if(x<y):
            print "("+str(z)+"="+str(y)+")>"+str(x)
        else:
            print "("+str(x)+"="+str(y)+")<"+str(x)
    elif(x==z):
        if(y<x):
            print "("+str(x)+"="+str(z)+")>"+str(y)
        else:
            print "("+str(x)+"="+str(z)+")<"+str(y)
    
else:
    if(b>x):
        x=b
    if(c>x):
        x=c
    if(x==a):
        y=b
        z=c
        if(c>y):
            y=c
            z=b
    elif(x==b):
        y=a
        z=c
        if(c>y):
            y=c
            z=a
    elif(x==c):
        y=a
        z=b
        if(b>y):
            y=b
            z=a
    print str(x)+">"+str(y)+">"+str(z)
