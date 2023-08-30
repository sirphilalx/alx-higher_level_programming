#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    tracker = 0
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
            tracker += 1
    except ValueError:
        pass
print()
