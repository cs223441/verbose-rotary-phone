'''
Given three arrays sorted in non-decreasing order, print all common elements in these arrays.

Examples: 

Input: 
ar1[] = {1, 5, 10, 20, 40, 80} 
ar2[] = {6, 7, 20, 80, 100} 
ar3[] = {3, 4, 15, 20, 30, 70, 80, 120} 
Output: 20, 80

Input: 
ar1[] = {1, 5, 5} 
ar2[] = {3, 4, 5, 5, 10} 
ar3[] = {5, 5, 10, 20} 
Output: 5, 5

'''
'''

@solution
new=[]

ar3 = [5, 5] 
ar1 = [1, 5, 5] 
ar2 = [3, 4, 5, 5, 10] 

first=len(ar1)        
second=len(ar2)        
third=len(ar3)        

if first>second and first>third:
    kc=first 
    nk=ar1

elif second>first and second>third:
    kc=second
    nk=ar2

elif third>first and third>second:
    kc=third 
    nk=ar3


for k in range(len(nk)):
    if nk[k] in ar1 and nk[k] in ar2 and nk[k] in ar3:
        new.append(nk[k])
for c in new:
    print(c,end="  ")

'''
