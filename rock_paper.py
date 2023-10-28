import random 
list=["rock", "paper" , "scissor"]
rand =random.choice(list)
user=str(input("enter the rock , paper or scissor "))
while(True):
    c=input("do you want to play (y or n) ")
    if(c=="y"):
        if rand==user:
            print("you are correct")
        else:
            print("you lost")
    else:
        print("thanks for playing")
