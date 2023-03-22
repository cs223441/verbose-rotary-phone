'''
5.(Find duplicates in O(n) time and O(1) extra space or Set 1)
Given an array of n elements that contains elements from 0 to n-1, with any of these numbers appearing any number of times. Find these repeating numbers in O(n) and using only.

Example: 

Input : n = 7 and array[] = {1, 2, 3, 6, 3, 6, 1}
Output: 1, 3, 6

Explanation: The numbers 1 , 3 and 6 appears more
than once in the array.

Input : n = 5 and array[] = {1, 2, 3, 4 ,3}
Output: 3

Explanation: The number 3 appears more than once
in the array.

@solution
------------
f=[12,3,5,67,83,23,3,4,3,56,4,23,4,523,5,5,6,7,84,5,2]
new=[]
a=0
for k in range(len(f)):
    if f.count(f[k])>1 and f[k] not in new:
        new.append(f[k])
for l in range(len(new)):
    d=new.pop()
    print(f" more than once occurance of no. : {d}")

'''