#Importing Modules
import sys

#Setting up initial data
try:
    an = int(input("how many Task would you like to manage?"))
except ValueError or NameError:
    print("you need to enter something numerically")
    sys.exit(1)
try:
    sl= int(input("How much sleep do you need?"))
except ValueError or NameError:
    print("you need to enter something numerically")
    sys.exit(1)
    
initial = {"TasksCount" : an,"Sleep" : sl}
rt= 24 - initial["Sleep"]
te= rt / initial["TasksCount"]

print(f"Times needed for every single task is {te}!")