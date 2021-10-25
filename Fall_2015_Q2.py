'''
Algorithm November 2015
Problem 2

Let I1, . . . , In be n intervals, where interval Ii is defined by set [ai, bi], i.e., starting from ai and
ending at bi. The interval scheduling problem asks to find a maximum number of disjoint intervals
that do not overlap with each other (for example, if four intervals are given as I1 = [1, 2], I2 =
[2, 3], I3 = [1, 4], I4 = [4, 5], then the solution is {I1, I2, I4}). Can you design a linear time greedy
algorithm to solve the interval scheduling problem? You can ignore the running time of your
algorithm in the pre-processing phase.


code - Wolf Walker
'''

I = [[1,2], [2,3], [1,4], [4, 5]]

### sort the list by starting time
I.sort(key=lambda x: x[0], reverse=False)
print(I)

i = 0 
time = 0 
job_list = []

while len(I) > i: 
    temp = I[i]
    if temp[0] >= time: 
        job_list.append(temp)
        time = temp[1]
    i+=1
    
print(job_list)
