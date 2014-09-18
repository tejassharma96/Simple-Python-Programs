p=0
n=input("Enter a number: \n")
m=n
o=n
while n!=1:
    if n%2!=0:
        n=n*3+1
        print n
    else:
        n/=2
        print n
    p+=1
    if n>m:
        m=n

print "Original value: " + `o`
print "Path length: " + `p`
print "Maximum value: " + `m`
