#!/usr/bin/python3.6

#Help Function
def menu():
    print("What should we use at the store ?\n")
    print("Enter 'DONE' to stop adding items")
    print("Enter 'HELP' to show all instruction in our app ")
    print("Enter 'SHOW' to show all items in our shopping list")
    print("Enter 'REMOVE' to remove item  in our shopping list")
    print("Enter 'EDIT' for edit item  in our shopping list")
    print("Enter 'EDITCAT' for edit category  in our shopping list\n")


def init_list_of_item():
    items.append(list())

def add_category(category_name):
    category.append(category_name);
    init_list_of_item()

def edit_category():
    answer=input("Enter your category name for rename it --> ")
    if answer in category:
        answer_rename=input("Enter your name for change {} --> ".format(answer))
        print("category {} rename to {} ".format(category[category.index(answer)],answer_rename))
        category[category.index(answer)]=answer_rename

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


def remove_item(answer):
    for cat in range(0,len(category)):
        if answer in items[cat]:
            while True:
                verify=input("are you sure to removing {} from  '{}'   yes/no --> ".format(answer,category[cat])).lower()
                if(verify == 'yes'): 
                   items[cat].remove(answer)
                   print("{} deleted from your {} category ".format(answer,category[cat]))
                   break
                elif (verify == 'no'):
                   break
                else:
                   print("Please Enter yes/no")
        else:
           print("{} not exist in your {} list".format(answer,category[cat]))


def edit_item(answer):
       for cat in range(0,len(category)):
          if answer in items[cat]:
            items[cat][items[cat].index(answer)]=input("Enter your changes for edit {} item form {}--> ".format(answer,cat))
          else:
            print("{} not Exist IN CAtegory {} ".format(answer,cat))
            break


def show():
    """
       show shopping list
       And category
    """
    print("My shopping list is")
    for cat  in range(0,len(category)):
        print("-------------------\nCategory Name: " + category[cat]+"\n-------------------")
        for item in items[cat]:
            print(item)


items=list()
category=[]
menu()
while True:
    answer = input("Choose From Menu or Enter your Item -->  ").lower()
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
        elif answer == 'editcat':
            edit_category()
        else:
            add_item(answer)
