import sys

def find_max(list_1):
    if len(list_1) > 0:
        max_val = -sys.maxsize - 1
        for i in list_1:
            if i > max_val:
                max_val = i
        print(max_val)
    else:
        print("List is Empty")


list_1 = [10, 37, 47, 27, 4, 58]
find_max(list_1)
