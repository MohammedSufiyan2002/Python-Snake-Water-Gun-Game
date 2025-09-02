''' WE ALL HAVE PLAYED SNAKE,WATER & GUN GAME (ROCK,PAPER,SCISSORS) IN OUR CHILDHOOD. IF YOU HAVEN'T, GOOGLE THE RULES OF THIS GAME AND WRITE A PYTHON PROGRAM CAPABLE OF PLAYING THIS GAME WITH THE USER. '''

'''
inputs:-

1 = Snake
-1 = Water
0 = Gun

'''
import random

computer= random.choice([-1,0,1])
user= input("Enter Your Choice: ")
user_dict={"s":1,
        "w":-1,
        "g":0
        }

reverse_dict={1:"Snake", -1:"Water", 0:"Gun"}
user_num= user_dict[user]

# By now, we have two numbers(variables), user_num and computer.

print(f"You Chose {reverse_dict[user_num]}\nComputer Chose {reverse_dict[computer]}!")

if(computer == user_num):
    print("It's a Tie!")
else:
    if (computer == -1 and user_num == 1):
        print("You Won!")
    elif(computer == -1 and user_num ==0):
        print("You Lost!")
    elif (computer == 1 and user_num == -1):
        print("You Lost!")
    elif(computer == 1 and user_num == 0):
        print("You Won!")
    elif(computer == 0 and user_num == -1):
        print("You Won!")
    elif(computer == 0 and user_num == 1):
        print("You Lost!")
    else:
        print("!!! Something Went Wrong !!!")

