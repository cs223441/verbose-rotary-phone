'''
Q.Check if all rows of a matrix are circular rotations of each other
  Given a matrix of n*n size, the task is to find whether all rows are circular rotations of each other or not. 

Examples: 

Input: mat[][] = 1, 2, 3
                 3, 1, 2
                 2, 3, 1
Output:  Yes
All rows are rotated permutation
of each other.

Input: mat[3][3] = 1, 2, 3
                   3, 2, 1
                   1, 3, 2
Output:  No
Explanation : As 3, 2, 1 is not a rotated or 
circular permutation of 1, 2, 3

--------------
Solution
-----------------

f=[
 ['a','b','c','d'],
 ['d','a','b','c'],
 ['a','c','b','d'],
 ['b','c','d','a']]

real=[]
ind=[]
ans=[]

for u in range(len(f[0])):
    real.append(u)
a=0
ans=[]

rep=[]
for i in range(len(f)):
    for u in range(len(f[i])):
        ans.append(f[i][u])
        ind.append(f[i].index(f[i][u]))

tt=[]
for i in range(len(ans)):
    for j in range(len(ans)):
        if ans[i]==ans[j] and j>i:
            if ind[i]!=ind[j] and j>i:
                tt.append('yes')
            else:
                tt.append('no')
for u in tt:
    if 'no' in tt:
        print('No')
        break
    else:
        print('Yes')
        break                  
'''