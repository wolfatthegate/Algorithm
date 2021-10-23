''' 
November 2018 Algorithm 

Problem #3

The program sort the colored keys in 'r', 'b', 'w' order
when the array of colored keys is passed to SortColor Function

Author - Wolf Walker

'''

def SortColor(arr):
    
    r_ptr = 0
    w_ptr = len(arr)-1
    
    for i in range(w_ptr):
        if (r_ptr < w_ptr):
            if(arr[i]=='r'):
                temp = arr[i]
                arr[i] = arr[r_ptr]
                arr[r_ptr] = temp
                r_ptr += 1
            elif(arr[i]=='w'):
                temp = arr[i]
                arr[i] = arr[w_ptr]
                arr[w_ptr] = temp
                w_ptr -= 1
                i -= 1
        if i > w_ptr:
            return arr
        
    
A = ['b', 'r', 'r', 'w', 'b', 'b', 'r', 'w', 'w', 'b']
A = SortColor(A)

print(A)
