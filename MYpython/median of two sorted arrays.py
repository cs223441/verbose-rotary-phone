'''
4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:
Input: nums1 = [1,2], nums2 = [3,4] [1,2,3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
'''
#solution--->
#odd number of observation :: (n+1)/2
#even number of observation :: ((n/2)+(n/2)+1)/2
nums1 = [12,34] 
nums2 = [53,65,886,76]
new=[]
cnt=0
ad=nums1+nums2
for k in range(len(ad)):
    terms=k+1

if terms%2!=0:
    anst=(terms+1)/2
    print(f"Output:{anst}")
    anst=int(anst)
    print(f"median is :: {ad[anst-1]}")
else:
    terms=terms/2
    terms=int(terms)
    dd=ad[terms]
    ss=ad[terms-1]
    ans=(dd+ss)/2
    print("median ::",int(ans))
        
