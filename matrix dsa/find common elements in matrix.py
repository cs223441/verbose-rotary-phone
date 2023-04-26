'''
Given an m x n matrix, find all common elements present in all rows in O(mn) time and one traversal of matrix.

Example: 

Input:
mat[4][5] = {{1, 2, 1, 4, 8},
             {3, 7, 8, 5, 1},
             {8, 7, 7, 3, 1},
             {8, 1, 2, 7, 9},
            };

Output: 
1 8 or 8 1
8 and 1 are present in all rows.

------------------
#Solution:
------------------

mat=[[1,8],
     [1,8],
     [1,8],
     [1,8],
     [1,8]]
ans=[]
a=0
for p in range(len(mat[0])):
    tt=mat[0][p]
    for u in range(len(mat)):
      if tt in mat[u]:
         a+=1
         if a==4:
          ff=mat[0][p]
          if ff in ans:
            continue
          else:
           ans.append(ff)
    a=0 
if ans==[]:
  print("Nothing found common in matrix")
else:
  print('Output : ',end=" ")
  for f in ans:
    print(f,end=" ")

'''
