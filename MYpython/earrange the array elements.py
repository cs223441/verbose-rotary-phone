'''
1.(Move all negative numbers to beginning and positive to end) An array contains both positive and negative numbers in random order. Rearrange the array elements so that all negative numbers appear before all positive numbers.

Examples : 

Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
Output: -12 -13 -5 -7 -3 -6 11 6 5

Note: Order of elements is not important here.

#solution
a=[-12,35,-14,45,-12,61,-2,-3,-23,62,45,-67,76,-88,55]
new=[]
for l in range(len(a)):
    if a[l]<0:
        ppd=a[l]
        new.insert(0,ppd)
    else:
        ddp=a[l]
        new.append(ddp)
print(f"OUTPUT Array : {new} ")

'''