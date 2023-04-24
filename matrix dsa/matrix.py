#-----------------------------------------------------Matrix DSA-------------------------------------------------------------------#
# 10 problems
'''
Q1

Print a given matrix in spiral form

Difficulty Level : Medium
Last Updated : 17 Mar, 2023

Given a 2D array, print it in spiral form.

Examples: 

Input:  {
         {1,  2,   3,  4},
         {5,  6,   7,  8},
         {9,  10,  11, 12},
         {13, 14,  15, 16 }
         }
Output: 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10 
Explanation: The output is matrix in spiral format. 


Input: { {1,   2,   3,   4,  5,   6},

         {7,   8,   9,  10,  11,  12},
         {13,  14,  15, 16,  17,  18}}

Output: 1 2 3 4 5 6 12 18 17 16 15 14 13 7 8 9 10 11
Explanation: The output is matrix in spiral format.

'''
# Output: 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
#1,2,3,4,8,12,16,15,14,13,7, 6, 5, 11, 10, 9
'''
mt = [
    
[5, 6, 7, 8],
[1, 2, 3, 4],
[9, 10,11,12],
[13,14,15,16]

]


l=[]
lst=[]
ans=[]
for i in mt:
    for j in i:
        lst.append(j)

print(lst)
start=0
dest=0
step=0
fp=0
a=0
b=0
tt=[1,2]
if fp==0 or fp%2==0:
     joint=mt[0]

elif fp%2!=0:
  joint=mt

while ans!=lst:
    if len(l)==0:
        l.append(fp)  
        if len(l)==2:
'''
'''
a=[[1,  2,  3, 42, 4],
   [41, 12, 33,435, 24],
   [5,  6,  7, 453, 8],
   [9,  10, 11,465, 12],
   [13, 14, 15,453, 16]]
'''
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

Given an n x n matrix and an integer x, find the position of x in the matrix if it is present. Otherwise, print “Element not found”. Every row and column of the matrix is sorted in increasing order. The designed algorithm should have linear time complexity

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

#solution
----------------
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
'''

'''
median : the middle value of the list is called median 
         if the no of all values is odd so total no of values/2 
         elif the no of all values is even so total no of values /2 and select the value which lies on the output term and go 1 step + and add both/2 == median

Q Find median in row wise sorted matrix
  We are given a row-wise sorted matrix of size r*c, we need to find the median of the matrix given. It is assumed that r*c is always odd.

Examples: 

Input: 1 3 5
        2 6 9
        3 6 9
Output: Median is 5
If we put all the values in a sorted 
array A[] = 1 2 3 3 5 6 6 9 9)

Input: 1 3 4
       2 5 6
       7 8 9
Output: Median is 5
Recommended Practice

#Solution
------------------
mt=[
[1,3,4],
[2,5,6],
[7,8,9]
]

f=[]
for k in mt :
    for l in k:
        f.append(l)
f=sorted(f) 
ans_index=len(f)/2
ans=f[ans_index.__floor__()]
print(f"Output:Median is {ans}")

'''

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
            print(f" row {k} has maximum 1s")
            break
'''
'''
Print all elements in sorted order from row and column wise sorted matrix
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

'''
'''
Q
Maximum size rectangle binary sub-matrix with all 1s
Given a binary matrix, find the maximum size rectangle binary-sub-matrix with all 1’s. 

Example: 

Input:

0 1 1 0
1 1 1 1
1 1 1 1
1 1 0 0

Output :
8
Explanation : 
The largest rectangle with only 1's is from 
(1, 0) to (2, 3) which is
1 1 1 1
1 1 1 1 

Input:
0 1 1
1 1 1
0 1 1      
Output:
6
Explanation : 
The largest rectangle with only 1's is from 
(0, 1) to (2, 2) which is
1 1
1 1
1 1

#Solution
-------------------
mt=[

[0, 1, 1, 0],
[1, 1, 1, 1],
[1, 1, 1, 1],
[1, 1, 0, 0]

]

def largest_rectangle_size(a):
    c=[]

    for i in range(len(mt)):
        c.append([])

    for u in range(len(c)):
        for t in range(len(mt[0])):
                c[u].append(0)

    dc=[]
    if len(mt)==len(c):

       if len(mt[0])==len(c[0]):
            ans=[]
            a=0
            for i in mt:
                if 0 in i:
                    continue
                else:
                    for l in i:
                        a=a+l
            ans.append(a)
            a=0
            for i in range(len(mt)):
                for j in range(len(mt[0])):
                    c[j][i]=mt[i][j]
            for k in c :
                if 0 in k:
                    continue
                else:
                    for g in k:
                        a=a+g
            ans.append(a)
            print(f"Output : {max(ans)}")
    else:
        raise IndexError("please provide m*n like input matrix")



largest_rectangle_size(mt)

'''
'''
Given a square matrix, turn it by 90 degrees in a clockwise direction without using any extra space.

Examples: 

Input:
1 2 3 
4 5 6
7 8 9  
Output:
7 4 1 
8 5 2
9 6 3

Input:
1 2
3 4
Output:
3 1
4 2 



#7 4 1 
#8 5 2
#9 6 3

#Solution:
------------------

e=[[1,2,3], 
   [4,5,6],
   [7,8,9]]  

def turn_90_degree(a):
    c=[]

    for i in range(len(e)):
        c.append([])

    for u in range(len(c)):
        for t in range(len(e[0])):
                c[u].append(0)


    for k in range(len(e)):
         for j in range(len(e[0])):
              c[j][k]=e[k][j]

    for u in c:
         for v in range(len(u)-1,-1,-1):
              print(u[v],end=" ")
         print()
turn_90_degree(e)    

'''
'''
Given an n x n matrix, where every row and column is sorted in non-decreasing order. Find the kth smallest element in the given 2D array.

Example, 

Input:k = 3 and array =
        10, 20, 30, 40
        15, 25, 35, 45
        24, 29, 37, 48
        32, 33, 39, 50 
Output: 20
Explanation: The 3rd smallest element is 20 

Input:k = 7 and array =
        10, 20, 30, 40
        15, 25, 35, 45
        24, 29, 37, 48
        32, 33, 39, 50 
Output: 30

Explanation: The 7th smallest element is 30


#Solution
--------------
d=[
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [24, 29, 37, 48],
    [32, 33, 39, 50] 

]
def find_kth_smallest_element(a):
    ac=[]

    k=int(input("Enter the term to find K'th smallest element : "))
    for i in a:
        for u in i:
            if u in ac:
                continue
            else:
                ac.append(u)

    if k>len(ac):
        raise (IndexError("Please Enter kth term under the length of given matrix and try again"))
    elif k==0:
        raise(ValueError("Please Enter value more than '0'"))
    ac=sorted(ac)
    print(ac)
    print(f'Output:{ac[k-1]}')

find_kth_smallest_element(d)


'''

w=[
[1, 2, 1, 14, 8],
[3, 7, 8, 14, 1],
[8, 7, 7, 14, 1],
[8, 1, 2,  5 , 9]
]
ff=[]
rr=0
for i in range(len(w[0])):
    gh=w[0][i]
    for u in w:
        if gh in u:
            rr+=1
            if rr==4:
                print(gh)
            else:
                i+=1

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

'''
'''
Given two matrices, the task is to multiply them. Matrices can either be square or rectangular:

Examples: 

(Square Matrix Multiplication)

Input: mat1[m][n] = { {1, 1}, {2, 2} }
mat2[n][p] = { {1, 1}, {2, 2} }
Output: result[m][p] = { {3, 3}, {6, 6} }

(Rectangular Matrix Multiplication)

Input: mat1[3][2] = { {1, 1}, {2, 2}, {3, 3} }
mat2[2][3] = { {1, 1, 1}, {2, 2, 2} }
Output: result[3][3] = { {3, 3, 3}, {6, 6, 6}, {9, 9, 9} }
'''
'''
Check if all rows of a matrix are circular rotations of each other
Read
Discuss
Courses
Practice
Video

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
'''
#
#m = [[1, 2, 1, 4, 8],
#     [3, 7, 8, 4, 1],
#     [8, 7, 7, 4, 1],
#     [8, 1, 2, 4, 9]
#     ]
#