import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

for d in d:
    __import__('pprint').pprint()
def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    apple_count = 0
    orange_count = 0
    
    for i in apples:

        iii = i + a

        if iii >= s and iii <= t:
            
            apple_count= apple_count+1
        #import code # TODO
        #code.interact(local=dict(globals(), **locals())) # TODO

    for j in oranges:

        jjj = j + b

        if jjj >= s and jjj <= t:
            orange_count= orange_count+1

    print(apple_count,orange_count, sep='\n')
    #return apple_count, orange_count


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0]) # house's cordinate (left)

    t = int(first_multiple_input[1]) # house's cordinate (right)




    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0]) # apple tree's cordinates

    b = int(second_multiple_input[1]) # orange tree's cordinates



    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0]) # number of apple

    n = int(third_multiple_input[1]) # number of orange

    apples = list(map(int, input().rstrip().split())) # cordinates of fallen apples

    oranges = list(map(int, input().rstrip().split())) #cordinates of fallen oranges

    countApplesAndOranges(s, t, a, b, apples, oranges)

