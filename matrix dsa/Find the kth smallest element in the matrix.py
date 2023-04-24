'''
Q.Given an n x n matrix, where every row and column is sorted in non-decreasing order. Find the kth smallest element in the given 2D array.

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
'''

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


