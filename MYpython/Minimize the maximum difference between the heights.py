'''
4.(Minimize the maximum difference between the heights)

Given the heights of N towers and a value of K, Either increase or decrease 
the height of every tower by K (only once) where K > 0. After modifications,the task is to minimize the difference between the heights
of the longest and the shortest tower and output its difference.

Examples: 

Input: arr[] = {1, 15, 10}, k = 6
Output:  Maximum difference is 5.
Explanation: Change 1 to 7, 15 to 9 and 10 to 4. Maximum difference is 5 (between 4 and 9). We can't get a lower difference.

Input: arr[] = {1, 5, 15, 10}, k = 3   
Output: Maximum difference is 8, arr[] = {4, 8, 12, 7}

@solution
k=4
ar=[1,7,6,4]
a=0
modified=[4,8,12,7]
diff=[]
for c in range(len(modified)):
    for k in range(len(modified)):
        we=modified[a]-modified[k]
        diff.append(we)
    a+=1

mx=max(diff)
mn=min(diff)

difference=mx-mn
j=mn+difference

print(f"Now the minimum is {j} and maximum is {mx}")

out=max(diff)
print(f"maximum difference :: {out}")


'''