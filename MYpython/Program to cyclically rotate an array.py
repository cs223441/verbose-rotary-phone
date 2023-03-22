'''
3.(Program to cyclically rotate an array by one)
Given an array, cyclically rotate the array clockwise by one. 

Examples:  

Input:  arr[] = {1, 2, 3, 4, 5}
Output: arr[] = {5, 1, 2, 3, 4}

@solution
arr=[1,2,3,4,5]
def rotate(arr):
    new=[]
    r=arr.pop()
    arr.insert(0,r)
    print(arr)

for k in range(5):
    rotate(arr)

''' 