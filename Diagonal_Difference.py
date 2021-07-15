import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    a = 0
    b = 0

    for i in range(n):

        a = a + arr[i][i]
    
    for j in range(n):
        

        b = b + arr[j][n-1-j]
    final = a-b
    if final > 0:
        pass
    elif final < 0:
        final = final* -1 
        
    else :
        pass
    return final

    # Write your code here

if __name__ == '__main__':

    #os.system('clear')


    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout
    

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))


    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
