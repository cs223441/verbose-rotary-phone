'''
Q2
Search in a row wise and column wise sorted matrix
Difficulty Level : Medium
Last Updated : 19 Sep, 2022
Read
Discuss(220+)
Courses
Practice
Video

Given an n x n matrix and an integer x, find the position of x in the matrix if it is present. Otherwise, print “Element not found”. 
Every row and column of the matrix is sorted in increasing order. The designed algorithm should have linear time complexity

Examples: 

Input: mat[4][4] =           { {10, 20, 30, 40},  x = 29
                               {15, 25, 35, 45},
                               {27, 29, 37, 48},
                             {32, 33, 39, 50}}
 
Output: Found at (2, 1)
Explanation: Element at (2,1) is 29

Input : mat[4][4] = { {10, 20, 30, 40},   x = 100
                                {15, 25, 35, 45},
                               {27, 29, 37, 48},
                              {32, 33, 39, 50}};
     
Output: Element not found
Explanation: Element 100 does not exist in the matrix
'''
#solution
#----------------
x = 33
a= [
   [10, 20, 30, 40],
   [15, 25, 35, 45],
   [27, 29, 37, 48],
   [32, 33, 39, 50]
]
 
for k in range(len(a)):
    for c in range(len(a[k])):
        if a[k][c]==x:
            print(f'found at : {k+1} row , {c+1} collumn')
            exit()
    if k==len(a)-1 and a[k][c]!=x:
        print("element not found ")
