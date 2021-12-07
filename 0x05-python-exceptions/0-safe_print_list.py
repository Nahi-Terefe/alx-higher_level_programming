#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        counter = 0
        for i in my_list:
            if counter < x:
                print("{}".format(i), end='')
                counter += 1
        print('')
        return counter
    except SyntaxError:
        print("Error Syntax")
