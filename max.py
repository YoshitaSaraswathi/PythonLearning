import sys
list_1=[10,37,47,27,4,58]
max= -sys.maxsize-1
if len(list_1)>0:
    for i in list_1:
        if i > max:
            max = i

    print(max)

else:
    print("List is Empty")
