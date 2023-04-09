'''
zigzag fashion:
Input: N = 7 , arr[] = {4,3,7,8,6,2,1} 
Output: arr[] = {3, 7, 4, 8, 2, 6, 1}
Explanation: The given array is in zig-zag pattern as we can see 
3 < 7 > 4 < 8 > 2 < 6 >1

Input: N = 4 , arr[] = {1, 4, 3, 2} 
Output: arr[] = {1, 4, 2, 3}
Explanation: The given array is in zig-zag pattern as we can see 1 < 4 > 2 < 3
'''
'''
@solution

a=[1, 4, 3, 2]
p=0
r=1
q=2

for k in range(len(a)-2):
    if a[r]<a[p]:
        swap=a[r]
        a[r]=a[p]
        a[p]=swap
    elif a[r]<a[q]:
        swap=a[r]
        a[r]=a[q]
        a[q]=swap
    else:
        p+=2
        r+=2
        q+=2

print(f" Output : {a}")

'''