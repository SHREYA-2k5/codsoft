#TASK 2 CALCULATOR -------- codsoft 
a=int(input("enter the inp1:"))
b=int(input("enter the inp2:"))
# calculator using users choice
print("1.addition 2.subtraction 3.multiplication 4.division")
ch=int(input("enter your choice:"))
if ch==1:
    c=a+b
    print("addition is:",c)
elif ch==2:
    c=a-b
    print("subtraction is:",c)
elif ch==3:
    c=a*b
    print("multiplication is:",c)
elif ch==4:
    c=a/b
    print("division is:",c)
else:
    print("reminder is:",a%b)