'''
Algorithm November 2018 

Problem #1

Moore's algorithm only works if the majority sample 
is larger than 50% of the entire sample

Author - Wolf Walker

'''

lst = [8, 4, 8, 5, 8, 8, 3, 4, 8, 8, 5, 8, 7, 8]

n = len(lst)
res = 0
count = 1

for i in range(1, n-1):
    if lst[res] == lst[i+1]:
        count += 1
    else:
        count -= 1
    
    if count == 0:
        res = i+1
        count += 1
    
print('the most frequent number is {}'.format(lst[res]))
