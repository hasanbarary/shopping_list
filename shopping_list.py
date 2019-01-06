#!/usr/bin/python3.6

#Help Function
def menu():
    print("What should we use at the store ?\n")
    print("Enter 'DONE' to stop adding items")
    print("Enter 'HELP' to show all instruction in our app ")
    print("Enter 'SHOW' to show all items in our shopping list")
    print("Enter 'REMOVE' to remove item  in our shopping list\n")
#Apend Function 
def append_list(items,answer):
    if answer not in items:
        items.append(answer)
        print("you added {} into your list. Now you have {} items".format(answer,len(items)))
    else:
        print("{} repeated".format(answer))
def remove_item(items,answer):
        if answer in items:
            items.remove(answer)
            print("{} deleted from your shopping list ".format(answer))
        else:
            print("{} not exist on shopping list".format(answer))
#main
items=[]
menu()
while True:
    answer = input("Choose From Menu -->").lower()
    if answer == 'help':
        menu()
    elif answer == 'done':
        break
    elif answer == 'show':
        print(items)
    elif answer == 'remove':
        answer = input("Enter your Item For Delete -->  ").lower()
        remove_item(items,answer)
    elif answer == '':
        continue
    else:
        append_list(items,answer)
