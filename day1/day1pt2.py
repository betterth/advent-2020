# day 1 part 2

import itertools
from functools import reduce
import operator

def main():
    input_list = []
    # Read input
    with open('input1.txt', 'r') as inputtxt:
        for line in inputtxt:
            input_list.append(int(line.rstrip()))
    # 
    two_tuple = check(input_list,2)
    three_tuple = check(input_list,3)
    print(two_tuple," ",three_tuple)
    print(product(two_tuple)," ",product(three_tuple))

def check(input_list,r):
    result = itertools.combinations(input_list,r)
    for iteration in result:
        if sum(iteration) == 2020:
            return iteration 

def product(iterable):
    return reduce(operator.mul, iterable, 1)

if __name__ == "__main__":
    main()