#!/bin/python3.4
from help import print_help
from list_append import append_list
shopping_list=[]
print_help()
#print('test')
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