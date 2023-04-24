'''
Q. Maximum size rectangle binary sub-matrix with all 1s
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
'''
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

