'''
Q Given a matrix of distinct values and a sum. The task is to find all the pairs in a given matrix whose summation is equal to the given sum. 
  Each element of a pair must be from different rows i.e; the pair must not lie in the same row.

Examples:  

Input : mat[4][4] = {{1, 3, 2, 4},
                     {5, 8, 7, 6},
                     {9, 10, 13, 11},
                     {12, 0, 14, 15}}
        sum = 20
Output: (1, 10), (3, 8), (2, 9), (4, 7), (11, 0) 

---------------
Solution:
-------------------
sm = 25
ff=[]
first=0
r=[[1, 3, 2, 4],
   [5, 8, 7, 6],
   [9, 10, 13, 11],
   [12, 0, 14, 15]]
for u in range(len(r)):
     jo=r[u]
     ind=u
     for t in range(len(jo)):
          elem=jo[t]
          for ut in range(ind+1,len(r)):
               for m in range(len(r[ut])):
                    if elem+r[ut][m]==sm:
                         ff.append((elem,r[ut][m]))
                    
if ff==[]:
     print("Output: No pair found")
else:
     print('Output:',end=" ")
     for i in ff:
          print(i,end=" ")
'''
