# TASK-4 Rock-Paper-Scissors Game 
print("welcome to rock paper scissors game")
print("1.rock 2.paper 3.scissors")
#getting input from user and comp
user=int(input("enter the choice:"))
comp=int(input("enter the choice:"))
if(user==1 and comp==1 or user==2 and comp==2 or user==3 and comp==3):
    print("REGAME SORRY NONE WON !!!")
elif(user==1 and comp==2 or user==2 and comp==1):
    print(" congratss paper won !!!!")
elif(user==2 and comp==3 or user==3 and comp==2):
    print("congrats scissors won!!!")
elif(user==1 and comp==3 or user==3 and comp==1):
    print("congrats rock won!!!")
else:
    print("WANNA PLAY AGAIN ")
