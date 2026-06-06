
# Online Python - IDE, Editor, Compiler, Interpreter

#Password Generator

import random
num_letters=["a","b","c","d","e","f","g","h","i","g","k","l","m","n","o","p","q","r","s","t","u","v",'w','x',"y","z"]
num_numbers = ['1','2','3','4','5','6','7','8','9','10']

num_symbols=['!','*','&','^']

print("Welcome to the password Generator")
letters = int(input("How many letters would you like in your password\n"))
numbers =int(input("How many numbers would you like to password\n"))
symbols = int(input("How many symbols would you like in your password\n"))

password= "" # password needs to exist 

for char in range(0, letters,+1):
  password+= random.choice(num_letters)
  
for char in range(0,numbers,+1):
  password+= random.choice(num_numbers)

for char in range(0,symbols,+1):
  password+= random.choice(num_symbols)
  
  print(password)
 
