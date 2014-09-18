#ask for number of lines
x=input("Please enter a number: \n")
#give default value to no. of stars and no. of spaces
st=1
sp=x
#loop printing in range of number of lines, giving christmas tree effect
#by reducing number of lines
for i in range(x):
    if i>=(x-3):
        #for last three lines go thin to give trunk effect
        if x>=18:
            st=5
            sp=x-2
        elif x<18:
            st=3
            sp=x-1
    elif i%3==0 and i>1 and i<6:
        #if divisible by 3 and between 1 and 6 reduce no. of stars by 2
        st-=2
        sp+=1
    elif i%3==0 and i>=6 and i<18:
        #if divisible by 3 and between 6 and 18 reduce no. of stars by 4
        st-=4
        sp+=2
    elif i%3==0 and i>=18:
        #if divisible by 3 and more than 18 reduce no. of stars by 6
        st-=6
        sp+=3
    print " "*sp+"*"*st
    st+=2
    sp-=1
