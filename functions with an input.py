def goodbye():
    print  ("see you later")
    print("i'll see you another time")
    
goodbye()


#functions with inputs 
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"hi how are you {name} ")
    
greet_with_name("David")
    
    
age = int(input("Enter your current age"))
 

def life_in_weeks():
    
    print(f"you have {age} weeks left.")

life_in_weeks()


#function with more than 1 input
def greet_with(name,location):
    print(f"Hello i'm {name} and i'm from {location}")
    
greet_with(name= "Harry", location= "Germany")
greet_with(name="Jason", location= "London")
