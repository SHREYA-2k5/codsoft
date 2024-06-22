#password generator task 3
import random
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower="abcdefghijklmnopqrstuvwxyz"
numb="0123456789"
symbols="@#*"
string=upper+lower+numb+symbols
length=int(input("enter the length:"))
passwordd="".join(random.sample(string,length))
print("your password is:",passwordd)