#!/usr/bin/python3.6

#Help Function
def menu():
    print("What should we use at the store ?\n")
    print("Enter 'DONE' to stop adding items")
    print("Enter 'HELP' to show all instruction in our app ")
    print("Enter 'SHOW' to show all items in our shopping list")
    print("Enter 'REMOVE' to remove item  in our shopping list")
    print("Enter 'EDIT' for edit item  in our shopping list\n")
#Apend Function 
def add_item(items,answer):
    if answer not in items:
        items.append(answer)
        print("you added {} into your list. Now you have {} items".format(answer,len(items)))
    else:
        print("{} repeated".format(answer))
def remove_item(items,answer):
        if answer in items:
            while True:
                verify=input("are you sure to removing {} item yes/no --> ".format(answer)).lower()
                if(verify == 'yes'): 
                   items.remove(answer)
                   print("{} deleted from your shopping list ".format(answer))
                   break
                elif (verify == 'no'):
                   break
                else:
                   print("Please Enter yes/no")
        else:
           print("{} not exist in your shopping list".format(answer))
def edit(items,answer):
       if answer in items:
           items[items.index(answer)]=input("Enter your changes for edit {} item -->".format(answer))
       else:
           print("{} not Exist.".format(answer))
#main
items=[]
menu()
while True:
    answer = input("Choose From Menu or Enter your Item -->").lower()
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
    elif answer == 'edit':
        answer = input("Enter your Item For Edit -->  ").lower()
        edit(items,answer)
    else:
        add_item(items,answer)
