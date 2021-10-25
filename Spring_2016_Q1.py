'''
April 2016 Algorithm 

Problem 1 

For searching I just use brute force. 

def sort(arr)

The idea is to initialize a variable K to the highest power of 2 
in size of the array such as to compare elements that are K distant apart.
Swap the elements if they are not in increasing order.
Reduce K by half and repeat the process until K becomes zero.

Wolf Walker

'''

import math

def findnum(arr, x):
    for i in range(len(arr)): 
        if arr[i] == x: 
            return True
    return False

def sort(arr):
    
    n = len(arr)
    k = int(math.log(n,2))
    k = pow(k,2)
    
    while k > 0: 
        
        i = 0
        while i+k < n:
            
            if arr[i] > arr[i+k]: 
                temp     = arr[i]
                arr[i]   = arr[i+k]
                arr[i+k] = temp 
            i += 1 
        k = int(k/2)
        
    print(arr)
        
    
A = [5, 20, 30, 40, 36, 33, 25, 15, 10]    
print('found' if findnum(A, 31) else 'not found')
sort(A)
