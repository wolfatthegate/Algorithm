'''
 Preliminary Exam Algorithm April 2019
 Question 1
 Inversion 

Author - Wolf Walker
'''

#   [0, 1, 2, 3, 4]
a = [2, 3, 8, 6, 1]

invr = []

for i in range(0, len(a)):
    for j in range(i+1, len(a)):
        if i < j and a[i] > a[j]:
            invr.append([i, j])

print(invr)
