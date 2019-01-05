#!/bin/python3.4

#Help Function
def print_help():
    print("What should we use at the store ?\n")
    print("Enter 'DONE' to stop adding items")
    print("Enter 'HELP' to show all instruction in our app ")
    print("Enter 'SHOW' to show all items in our shopping list")

#Apend Function 
def append_list(shopping_list,answer):
    if answer not in shopping_list:
        shopping_list.append(answer)
        "{} Added Into List ".format(answer)
    else:
        "{} repeated".format(answer)
        
#main
shopping_list=[]
print_help()
while True:
    answer = input().lower()
    if answer == 'help':
        print_help()
    elif answer == 'done':
        break
    elif answer == 'show':
        print(shopping_list)
    else:
        append_list(shopping_list,answer)
