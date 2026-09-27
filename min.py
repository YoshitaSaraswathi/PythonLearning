import sys
list_1=[10,37,47,27,4,58]
min= sys.maxsize
if len(list_1)>0:
    for i in list_1:
        if i < min:
            min = i

    print(min)

else:
    print("List is Empty")
