
# Online Python - IDE, Editor, Compiler, Interpreter
import random # module used to genrate random numbers 


#random_integer = random.randint(1,10) # prints out a number at random
#print(random_integer)

#random_number_0_to_1= random.random()
#print(random_number_0_to_1)

random_heads_or_tails = random.randint(0,1)

if random_heads_or_tails == 0:
    print("heads")
else:
    print("Tails")
print(random_heads_or_tails )


#lists

#states_of_America = ["new jersey", "virginia", "new york ", "boston"]
#states_of_America[1] = "north carolina"
#states_of_America.append("Brazil")# adds an item to the end of the list 
#.extend just extends the list
#print(states_of_America)

friends = ["Alice", "Bob", "charlie","David", "Emannuel"]
print(random.choice(friends))
