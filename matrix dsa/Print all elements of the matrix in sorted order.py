'''
Q. Print all elements in sorted order from row and column wise sorted matrix
   Given an n x n matrix, where every row and column is sorted in non-decreasing order. Print all elements of the matrix in sorted order.

Example: 

Input: mat[][] = {         {10, 20, 30, 40},
                           {15, 25, 35, 45},
                           {27, 29, 37, 48},
                           {32, 33, 39, 50},
                   };
Output: 10 15 20 25 27 29 30 32 33 35 37 39 40 45 48 50

#Solution
-----------------
'''
mat = [
        [10, 20, 30, 40],
        [15, 25, 35, 45],
        [27, 29, 37, 48],
        [32, 33, 39, 50],
      ]
ans=[]
for i in mat:
    for u in i:
        ans.append(u)
ans=sorted(ans)
print(f"Output : {ans}")
