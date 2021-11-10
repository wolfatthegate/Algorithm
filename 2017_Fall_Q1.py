'''
November 2017
Problem #1
'''
import math

T = [-12, -8, -3, 2, 3, 5, 11, 18]
min = 0
max = len(T)-1
pivot = int((min+max)/2)
counter = 0
found = False

while counter < math.log(len(T),2):
    if T[pivot] == pivot:
        found = True
        print('index found: {}'.format(pivot))
        break
    else:
        if pivot < T[pivot]:
            max = pivot
        else: # pivot > T[pivot]
            min = pivot
        pivot = int((min+max)/2)
    counter =+ 1
    
if found == False:
    print('index not found')
