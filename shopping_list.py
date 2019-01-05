#!/bin/python3.4
def print_help():
    print("What should we use at the store ?\n")
    print("Enter 'DONE' to stop adding items")
    print("Enter 'HELP' to show all instruction in our app ")
    print("Enter 'SHOW' to show all items in our shopping list")

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
