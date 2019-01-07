#!/usr/bin/python3.6

#Help Function
def menu():
    print("What should we use at the store ?\n")
    print("Enter 'DONE' to stop adding items")
    print("Enter 'HELP' to show all instruction in our app ")
    print("Enter 'SHOW' to show all items in our shopping list")
    print("Enter 'REMOVE' to remove item  in our shopping list")
    print("Enter 'EDIT' for edit item  in our shopping list\n")

def init_list_of_item():
    items.append(list())
##########################################ADD CATEGORY################################################

def add_category(category_name):
    category.append(category_name);
    init_list_of_item()

##########################################ADD ITEM####################################################

def add_item(answer):
    print("Enter Your CATEGORY NAME")
    cat_name=input("--> ")
    if not cat_name in category:
        add_category(cat_name)
    if answer not in items[category.index(cat_name)]:
       items[category.index(cat_name)].append(answer)
       print("you added {0} into your list. Now you have {1} items ".format(answer,len(items[category.index(cat_name)])))
    else:
        print("{} repeated".format(answer))


#########################################REMOVE ITEM#################################################
def remove_item(answer):
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

#######################################EDIT ITEM######################################################

def edit_item(answer):
       if answer in items:
           items[items.index(answer)]=input("Enter your changes for edit {} item -->".format(answer))
       else:
           print("{} not Exist.".format(answer))

########################################SHOW ITEM#####################################################

def show():
    print("My shopping list is")
    for cat  in range(0,len(category)):
        print("###############\nCategory Name: " + category[cat]+"\n###############")
        for item in items[cat]:
            print(item)
###############################################MAIN###################################################
#main
#size=int(input("Enter Your Category Count --> "))
#items=init_list_of_item(size)
items=list()
category=[]
menu()
while True:
    answer = input("Choose From Menu or Enter your Item -->").lower()
    if not answer.isalpha():
        print("Your input Not alpha or have a numeric character")
        continue
    else:
        if answer == 'help':
            menu()
        elif answer == 'done':
            break
        elif answer == 'show':
            show()
        elif answer == 'remove':
            answer = input("Enter your Item For Delete -->  ").lower()
            remove_item(answer)
        elif answer == '':
            continue
        elif answer == 'edit':
            answer = input("Enter your Item For Edit -->  ").lower()
            edit_item(answer)
        elif answer == 'cat':
            add_category()    
        else:
            add_item(answer)
