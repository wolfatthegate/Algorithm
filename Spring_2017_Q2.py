'''

April 2017

Problem 2 

VLSI databases

This Algorithm requires more than O(n log n) but it checks whether 
two or more rectangles are overlapped. 

Given a list of rectangle coordinates

[16,3], [20,11]
[7, 5], [15,10]
[17,4], [19, 5]
[2, 2], [8, 6]
[10,6], [14, 9]

'''

def checkOverlap(R1, R2):
    ### Example arguments 
    ### R1 = [[2, 2], [8, 6]]   
    ### R2 = [[7, 5], [15,10]]
    
    R1low  = R1[0]  ### [2, 2]
    R1high = R1[1]  ### [8, 6]
    R2low  = R2[0]  ### [7, 5]
    R2high = R2[1]  ### [15,10]
    
    if R1low[0] < R2low[0] and R1high[0] > R2high[0]:
        if R1low[1] < R2low[1] and R1high[1] > R2high[1]:
            return True
        
    return False

### Sort the rectangle in ascending low x which is Recs[0][0]. It takes O(n log n) to sort the array. 

Recs = [[[2, 2], [8, 6]], [[7, 5], [15,10]], [[10,6], [14, 9]], [[16,3], [20,11]], [[17,4], [19, 5]]]

for x in range(len(Recs)-1):
    for y in range(x+1, len(Recs)):
        if checkOverlap(Recs[x], Recs[y]):
            print('{} is in {}'.format(Recs[y], Recs[x]))
