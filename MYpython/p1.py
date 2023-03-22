#Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo
'''
ar=[1,0,2]
ar=sorted(ar)
print(ar)
'''

#find the maximum and minimum element in the array
'''
#finding maximum::
j=[12,3,5,23,45,67,2,4,3,1,3,4,5,6,2]
j=sorted(j)
print(j)
print(f"maximum number is : {j[len(j)-1]}")

#finding minimum:
j=[12,3,5,23,45,67,2,4,3,1,3,4,5,6,2]
j=sorted(j)
print(j)
print(f"maximum number is : {j[0]}")

'''

#Revese Array
'''
o=[1,2,3,4,5,6]
for l in range(len(o)-1):
    for f in range(len(o)-1):
        if o[f]<o[f+1]:
            sw=o[f]
            o[f]=o[f+1]
            o[f+1]=sw
print(o)

'''

#find kth min element in the array
'''
f=[2,325,5,637,37,83,6,3,34,212,3,3,4,6,6,6,34,13,2]
i=int(input("Enter kth no :"))
new=[]
f=sorted(f)
g=0
for k in range(len(f)):
    if k>g and f[k]==f[g]:
        continue
    else:
        g=k
        ca=f[g]
        new.append(ca)
print(new)
print(f"{i}'th minimum no : {new[i-1]}")

'''

#find kth max element in the array
'''
f=[2,325,5,637,37,83,6,3,34,212,2]
i=int(input("Enter kth no :"))
new=[]
f=sorted(f)
g=0
for k in range(len(f)):
    if k>g and f[k]==f[g]:
        continue
    else:
        g=k
        ca=f[g]
        new.append(ca)
gc=len(new)
print(f"{i}'th minimum no : {new[gc-i]}")
'''
#19/1/2023
#questions:

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

'''
2.(Find Union and Intersection of two unsorted arrays)
Given two unsorted arrays that represent two sets (elements in every array are distinct), find the union and intersection of two arrays.

Example: 

arr1[] = {7, 1, 5, 2, 3, 6} 
arr2[] = {3, 8, 6, 20, 7} 
Then your program should print Union as {1, 2, 3, 5, 6, 7, 8, 20} and Intersection as {3, 6, 7}. Note that the elements of union and intersection can be printed in any order.


#definition of union :  all elements that found in both sets but should not repeat

@solution
-------------
new=[]
set1=[1,4,5,7,3,23]
set2=[4,32,4,6,734,7,78,3]
for l in range(len(set1)):
    if set1[l] in set2:
        continue
    else:
        set2.append(set1[l])
for c in range(len(set2)):
    if set2[c] in new:
        continue
    else:
        new.append(set2[c])
new=sorted(new)
print(f"set1:{set1}")
print(f"set2:{set2}")
print(f"Union of set1 and set2 is : {new}")


#intersection: all elements that are common in both the sets

@solution
---------------
new=[]
set1=[13,4,5,6,23,46,7,452,24,5,6,3,45,6,24,57,23,55,]
set2=[4,32,4,6,734,7,78,3,4,13,5,7,2,4,6,]
if len(set1)>len(set2):
    selected=set1 
    unselected=set2
else:
    selected=set2
    unselected=set1

for l in range(len(selected)):
    if selected[l] in unselected:
        if selected[l] in new:
            continue
        else:
            new.append(selected[l])
    else:
        continue
new=sorted(new)
print(f'Intersection of two sets : {new}')

'''
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
'''
6.(Merge two sorted arrays)
Given two sorted arrays, the task is to merge them in a sorted manner.
Examples: 

Input: arr1[] = { 1, 3, 4, 5}, arr2[] = {2, 4, 6, 8} 
Output: arr3[] = {1, 2, 3, 4, 4, 5, 6, 8}

Input: arr1[] = { 5, 8, 9}, arr2[] = {4, 7, 8} 
Output: arr3[] = {4, 5, 7, 8, 8, 9} 


@solution
--------------
one=[ 1, 3, 4, 5]
two=[2, 4, 6, 8]

merged=[]
for k in range(len(one)):
        merged.append(one[k])

for k in range(len(two)):
        merged.append(two[k])
merged=sorted(merged)

print(merged)

'''

#20/1/2023
#questions

'''

1.(Minimum number of jumps to reach end or Set 2 (O(n) solution))
Given an array of integers where each element represents the max number of steps that 
can be made forward from that element. Write a function to return the minimum number of 
jumps to reach the end of the array (starting from the first element). If an element 
is 0, then we cannot move through that element. If we can’t reach the end, return -1.

Examples: 

Input:  arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
Output: 3 (1-> 3 -> 8 -> 9)
'''
'''
Explanation: Jump from 1st element to 
2nd element as there is only 1 step, 
now there are three options 5, 8 or 9. 
If 8 or 9 is chosen then the end node 9 
can be reached. So 3 jumps are made.
Input  :  arr[] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1}
Output : 10

Explanation: In every step a jump is 
needed so the count of jumps is 10.
'''
'''
2.(Largest Sum Cont3iguous Subarray (Kadane’s Algorithm))Given an array arr[] of size N. The task is to find the sum of the contiguous subarray within a arr[] 
with the largest sum. 

kadane-algorithm
'''
#1=[-10]
#2=[1]
#3=[4]
#4=[0]
#5=[1]
#6=[3]
#7=[2]

'''
3.(Merge Overlapping Intervals)
Given a set of time intervals in any order, merge all overlapping intervals into one and output the result which should have only mutually exclusive intervals.

Example:

Input: Intervals = {{1,3},{2,4},{6,8},{9,10}}
Output: {{1, 4}, {6, 8}, {9, 10}}
Explanation: Given intervals: [1,3],[2,4],[6,8],[9,10], we have only two overlapping intervals here,[1,3] and [2,4]. 
Therefore we will merge these two and return [1,4],[6,8], [9,10].

Input: Intervals = {{6,8},{1,9},{2,4},{4,7}}
Output: {{1, 9}} 

4.(exicographically Next Permutation)

Given a set of time intervals in any order, merge all overlapping intervals into one and output the result which should have only mutually exclusive intervals.

Example:

Input: Intervals = {{1,3},{2,4},{6,8},{9,10}}
Output: {{1, 4}, {6, 8}, {9, 10}}
Explanation: Given intervals: [1,3],[2,4],[6,8],[9,10], we have only two overlapping intervals here,[1,3] and [2,4]. 
Therefore we will merge these two and return [1,4],[6,8], [9,10].

Input: Intervals = {{6,8},{1,9},{2,4},{4,7}}
Output: {{1, 9}} 

5.(Inversion count in Array using Merge Sort)
Inversion Count for an array indicates – how far (or close) the array is from being sorted. If the array is already sorted, 
then the inversion count is 0, but if the array is sorted in reverse order, the inversion count is the maximum. 

Given an array a[]. The task is to find the inversion count of a[]. Where two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.

Examples: 

Input: arr[] = {8, 4, 2, 1}
Output: 6
Explanation: Given array has six inversions: (8, 4), (4, 2), (8, 2), (8, 1), (4, 1), (2, 1).

Input: arr[] = {1, 20, 6, 4, 5}
Output: 5
Explanation: Given array has five inversions: (20, 6), (20, 4), (20, 5), (6, 4), (6, 5). 

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
'''
7.(Count pairs with given sum)
Given an array of N integers, and a number sum, the task is to find the number of pairs of integers in the array whose sum is equal to sum.

Examples:  

Input:  arr[] = {1, 5, 7, -1}, sum = 6
Output:  2
Explanation: Pairs with sum 6 are (1, 5) and (7, -1).

Input:  arr[] = {1, 5, 7, -1, 5}, sum = 6
Output:  3
Explanation: Pairs with sum 6 are (1, 5), (7, -1) & (1, 5).         

Input:  arr[] = {1, 1, 1, 1}, sum = 2
Output:  6
Explanation: Pairs with sum 2 are (1, 1), (1, 1), (1, 1), (1, 1), (1, 1).
Input:  arr[] = {10, 12, 10, 15, -1, 7, 6, 5, 4, 2, 1, 1, 1}, sum = 11
Output:  9
Explanation: Pairs with sum 11 are (10, 1), (10, 1), (10, 1), (12, -1), (10, 1), (10, 1), (10, 1), (7, 4), (6, 5).
'''
'''
#@solution
#q=[10, 12, 10, 15, -1, 7, 6, 5, 4, 2, 1, 1, 1]
#new=[]
#sm=11
#a=0
#cnt=0
#for k in range(len(q)):
#    for c in range(len(q)):
#        if q[a]+q[c]==sm and c>a:
#            cnt+=1
#    a+=1
#print(cnt)
'''
'''
2/4/2023

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
'''
Input: {4, 2, -3, 1, 6}
Output: true 
Explanation:
There is a subarray with zero sum from index 1 to 3.

Input: {4, 2, 0, 1, 6}
Output: true
Explanation: The third element is zero. A single element is also a sub-array.

Input: {-3, 2, 3, 1, 6}
Output: false
'''
'''
py=[]
v=[4,3,1,1,6]
for k in v:
    if k<0:
        py.append(k)

cnt=0
for i in range(len(py)):
    if type(py[i])==int:
        cnt+=1
for b in v:
    if b==0:
        print("true , exists already")
        exit()
    else: 
        pass

new=[]
try:
    for k in v:
        if k<0:
            target=k
        else:
            pass
        

    for c in range(len(v)):
         for m in range(len(v)):
            if v[c]+v[m] and m!=c:
               rt= v[c]+v[m]
               new.append(rt)            

    for l in new:
        if l+target==0:
            dc=l+target
            if dc==0:
                print("true")
            else:
                print("false")
            break
        else:
            continue

except NameError:
        print("no value is 0 or less than 0")
        exit()
'''
#2/9/2023
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

'''

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#target = 9
'''
target = 9
new=[]
nums = [2,7,11,12]
for k in range(len(nums)):
    for s in range(len(nums)):
        if nums[k]+nums[s] == target and s>k :
            new.append(k)
            new.append(s)
            print(new)
            break
        else:
            continue
'''
'''   
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21


@solution
--------------
c='12'
few=[]
for s in range(len(c)-1,-1,-1):
        if c[s]>'0':
              ll=s
              break

new=[]
for j in range(0,ll+1):
      new.insert(0,c[j])
ln=len(new)-1

if new[ln]=='-':
       
       few.insert(0,new[ln])

for c in range(len(new)):
        if new[c]=='-':
            continue
        else:
            few.append(new[c])
print(few)

for k in few:
      print(k,end="")
'''
'''
5. Longest Palindromic Substring
Given a string s, return the longest 
palindromic

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

'''
#s = "babad"
#Output: "bab"
'''
6. Zigzag Conversion

Medium
5.8K
11.8K
Companies
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:

Input: s = "A", numRows = 1
Output: "A"
'''
'''
Input: s = "PAYPALISHIRING", numRows = 4

P     I    N
A   L S  I G
Y A   H R
P     I

out: pinalsigyahrpi

'''
'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer 
range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 
Constraints:
-231 <= x <= 231 - 1


#Input: x = 120
#Output: 21

@solution
x =120
x=str(x)
ln=len(x)-1
l=[]
gg=[]
for k in x:
    l.append(k)

gp=len(l)-1

for  c in range(gp,-1,-1):
    if l[c]=='0':
        continue
    else:
        df=c        
        break
for  c in range(df+1):
    gg.insert(0,l[c])

gg2=[]
for k in gg:
    if k=='-' or k=='^' or k=='/' or k=='%' or k=='*':
        gg2.insert(0,k)

ee=""
for c in gg:
    if c not in gg2:
        gg2.append(c)
    else:
        continue
for l in gg2:
    ee=ee+l

ee=int(ee)
print(f"Ans:{ee}")
print(f"type of {ee} : {type(ee)}")

'''
'''
12. Integer to Roman
Medium
5.3K

Companies
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, 
which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

Example 1:

Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.
Example 2:

Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 3:

Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 
Constraints:

1 <= num <= 3999
    
I=1
V=5
X=10
L=50
C=100
D=500
M=1000

'''
#num = 58
#Output: "LVIII"
#n=58

'''
14. Longest Common Prefix
Easy
12.8K
3.8K
Companies
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 
Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.

'''
#Output: "fl"

s=["flower","flow","flight"]
new=[]
big=[]
for j in s:
    j=list(j)
    new.append(j)



