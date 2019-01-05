#!/usr/bin/python3.4
def append_list(shopping_list,answer):
    if answer not in shopping_list:
        shopping_list.append(answer)
        "{} Added Into List ".format(answer)
    else:
        "{} repeated".format(answer)