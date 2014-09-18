x=input("Enter the number of lines: \n")
st=1
sp=x
for i in range(x):
    print " "*sp+"*"*st+" "*sp
    st+=2
    sp-=1
