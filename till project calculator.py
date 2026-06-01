
# Online Python - IDE, Editor, Compiler, Interpreter
#number manpulation and F strings

#till project calculator 
print("Welcome to your tip calculator ")
bill =float(input("what was the total bill"))
tip = int(input("What percentage tip would you like to give? 10 12 15"))
people = int(input("How Many people should split the bill"))
print("Each person should pay ")
bill_with_tip = tip/100 * bill + bill
print(bill_with_tip)



