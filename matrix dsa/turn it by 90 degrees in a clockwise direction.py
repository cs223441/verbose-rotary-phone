'''
Q.Given a square matrix, turn it by 90 degrees in a clockwise direction without using any extra space.

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
'''
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

