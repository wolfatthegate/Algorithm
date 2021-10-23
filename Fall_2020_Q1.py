'''
Preliminary Exam Alogrithm  Dec 2020
Question #1

Longest None repeating substring
Author - Wolf Walker

'''

s = 'examation'

i = 0
j = 0
n = len(s)

lst = []

max_len = 0

while i < n: 
    c = s[i]
    while c in lst: 
        lst.remove(s[j])
        j+=1
    lst.append(c)
    max_len = i-j+1
    i+=1
        
print(lst)
print(max_len)
