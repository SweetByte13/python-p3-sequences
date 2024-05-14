#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci=[0,1,1,2,3,5,8,13,21,34]
    if length==1:
        print([fibonacci[0]])
    elif length==2:
        print(fibonacci[0:2])
    elif length == 10:
        print(fibonacci[0:10])
    else:
        print([])