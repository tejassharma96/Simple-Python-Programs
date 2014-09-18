a=input("Enter an a value: \n")
b=input("Enter a b value: \n")
while b!=0:
    temp=a
    a=b
    b=temp%b

print "GCD = " + `a`
