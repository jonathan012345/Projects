# project treasure island

print("Welcome to Treasure Island")
print("Your mission is to find the treasure")

choice1 = input("You're at a crossroad. Do you want to go left or right? ").lower()

if choice1 == "left":
    choice2 = input(
        "You've come to a lake. There is an island in the middle of the lake.\n"
        "Type 'wait' to wait for a boat or 'swim' to swim across: "
    ).lower()

    if choice2 == "wait":
        choice3 = input(
            "You arrive at a house with 3 doors: red, yellow, and blue.\n"
            "Which colour do you choose? "
        ).lower()

        if choice3 == "yellow":
            print("You found the treasure! You win!")
        elif choice3 == "red":
            print("You were burned by fire. Game over.")
        elif choice3 == "blue":
            print("You were eaten by beasts. Game over.")
        else:
            print("You chose a door that doesn't exist. Game over.")

    else:
        print("You were attacked by trout. Game over.")

else:
    print("You fell into a hole. Game over.")
    


        