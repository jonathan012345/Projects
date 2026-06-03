import random
# Online Python - IDE, Editor, Compiler, Interpreter
#rock paper scissiors

user_choice = int(input("What do you choose? Type 0 for rock, Type 1 for paper,Type 2 for scissors "))
computer_choice=random.randint(0,2)
print(f"Computer chose {computer_choice}")


if user_choice>= 3 or user_choice<0:
    print("you typed an invalid number")
    
    
elif user_choice >computer_choice:
    print("you win!")
    
elif computer_choice > user_choice:
    print("you lose!")
    
elif computer_choice == user_choice:
    print("it's a tie")
    
