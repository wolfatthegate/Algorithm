'''
 Preliminary Exam Algorithm - April 2017 
 Problem #1
 
 Determine whether there exists 2 elements in A such that the sum is x. 
 Author - Waylon Luo
 
'''
       
A = [5, 3, 22, 15, 25, 14, 8, 2]

### sorting takes O(n log n) 
A = sorted(A) 

### number of sum of two elements
x = 21

i = 0 
j = len(A) - 1

while i < j: 
    if x < A[i] + A[j]: 
        j -= 1
    elif x > A[i] + A[j]: 
        i += 1
    else: 
        print('found the numbers: {}, {}'.format(A[i], A[j]))
        quit()
        
print('No numbers found')

