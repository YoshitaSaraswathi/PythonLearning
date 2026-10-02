import sys

def find_min(list_1):
    if len(list_1) > 0:
        min_val = sys.maxsize
        for i in list_1:
            if i < min_val:
                min_val = i
        print(min_val)
    else:
        print("List is Empty")


list_1 = [10, 37, 47, 27, 4, 58]
find_min(list_1)
