'''
6.(Best Time to Buy and Sell Stock)
Given an array prices[] of length N, representing the prices of the stocks on different days, the task is to find the maximum 
profit possible for buying and selling the stocks on different days using transactions where at most one transaction is allowed.

Note: Stock must be bought before being sold.

Examples:

Input: prices[] = {7, 1, 5, 3, 6, 4]
Output: 5
Explanation:
The lowest price of the stock is on the 2nd day, i.e. price = 1. Starting from the 2nd day, the highest price of the stock is 
witnessed on the 5th day, i.e. price = 6. 
Therefore, maximum possible profit = 6 – 1 = 5. 

Input: prices[] = {7, 6 , 5 , 4 , 3 , 1} 
Output: 0
Explanation: Since the array is in decreasing order, no possible way exists to solve the problem.
'''
'''
@solution
c=[7, 6 , 5 , 4 , 3 , 1]
d=[]
mn=min(c)
ln=len(c)-1
new=[]

for m in range(len(c)):
    if c[m]==mn:
        gn=m

p=mn

for k in range(len(c)):   
    if c[k]==mn:
        gn=k
        if k>gn and c[gn]<c[k]:
            asc="this is in descending order"
            new.append(asc)
    elif c[ln]==mn:
        print("possible profit : 0")
        exit()
    else:
        if k>gn:
            d.append(c[k])
mx=max(d)
print(f"possible profit : {mx-mn}")
'''
