'''
 Preliminary Exam Algorithm April 2019
    
 Question 2 

 *** use greedy algorithm
 
 - sort the job by highest profit
 - pick up the highest profit job and check the deadline
 - if the job meets the deadline, add it to the queue
 - update the time
 - repeat the last three steps. 
 
 Author 
 @WolfWalker

'''
#   each job has [processing time, maximum profit, deadline]
#   [a[0]    ,a[1]   ,a[2]   ,a[3]   ,a[4]    ]
#    
a = [[5,3,10],[4,6,9],[7,2,5],[3,4,8],[8,3,16]]

### sorting will take O(n log n) time
sorted_a = sorted(a, key = lambda x: x[1])
print('available jobs:', sorted_a)

jobs = []
time = 0 

### while loop takes O(n) time for every jobs. 
while len(sorted_a) > 0: 
    temp = sorted_a.pop()
    if time < temp[2]: 
        jobs.append(temp)
        time += temp[0]

print('eligible jobs :', jobs)
print('maximum profit: ', sum(j[1] for j in jobs))

