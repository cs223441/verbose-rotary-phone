'''
Maximum Product Subarray or Set 3

Difficulty Level : Hard
Given an array A[] that contains both positive and negative integers, find the maximum product subarray.

Examples : 

Input: A[] = {6, -3, -10, 0, 2}
Output: 180  // The subarray is {6, -3, -10}

Input: A[] = {-1 , -3 , -10 , 0 , 60 }
Output: 60  // The subarray is {60}

Input: A[] = { -2, -3, 0, -2, -40 }
Output: 80  // The subarray is {-2, -40}

#@solution
ee=[]
f=[]
f2=[]
e=[ -1 , -3 , -10 , 0 , 60 ]
big=[]
mx=max(e)
print(e)
a=0
for l in range(len(e)):
    if e[l]==0:
       a=l
for u in range(a):
     f.append(e[u])

for k in range(len(e)):
    if e[k] in f and k<a or e[k]==0:
        continue
    else:
        f2.append(e[k])

big.append(f)
big.append(f2)

if len(e)<=3:
    print(f"out:{mx}")
else:

    import math as mt

    nigga=[]
    for l in range(len(big)):
        rt=mt.prod(big[l])
        nigga.append(rt)

    print(f'Out : {max(nigga)}')

    for p in range(len(big)):
        if mt.prod(big[p])==max(nigga):
            print(f"Subarray:{big[p]}")
'''

