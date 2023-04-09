
#transposing matrix:
a=[ [1,323,17],
    [2,4,12],
    [5,2,125], 
    [3,5,73]]

c=[[0,0,0,0],
   [0,0,0,0],
   [0,0,0,0]]  

for i in range(len(a)):
    for j in range(len(a[0])):
        c[j][i]=a[i][j]

h=[
    [3,5,7],
    [4,7,2],
    [5,7,2]
]

f=[
[0,0,0],
[0,0,0],
[0,0,0]
]

for i in range(len(h)):
    for u in range(len(h[0])):
        f[u][i]=h[i][u]
print(h)
print(f)
