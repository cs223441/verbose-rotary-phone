'''
Find the row with maximum number of 1s
Given a boolean 2D array, where each row is sorted. Find the row with the maximum number of 1s. 

Example:  

Input matrix :          0 1 1 1
                        0 0 1 1
                        1 1 1 1  // this row has maximum 1s
                        0 0 0 0
Output: 2

Recommended Practice

#solution
------------------
'''
mt=[
   [0,1,1,1],
   [0,0,1,1],
   [1,1,1,1],  
   [0,0,0,0]
   ]
cnt=[]
for k in range(len(mt)):
    for j in range(len(mt[k])):
        ct= mt[k].count(1)
    cnt.append(ct)

for k in range(len(mt)):
    for j in range(len(mt[k])):
        if mt[k].count(1)==max(cnt):
            print(f" row {k+1} has maximum 1s")
            break

