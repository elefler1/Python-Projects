# 1. DEFAULT Arguments = Default values that can be assigned to function parameters
#                     If no value is provided for the parameter, the default value is used 
#                     Making your functions more flexible reduces the # of args
#                       1. Positional Arguments
#                       2. DEFAULT Arguments
#                       3. Keyword Arguments
#                       4. Arbitrary Arguments

def net_price(list_price, discount=0, tax=0.07):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 0.1, 0.05))

import time

def count(end, start=0):
    for x in range(start, end + 1):
        print(x)
        time.sleep(1)
    print("DONE!")

count(10)

