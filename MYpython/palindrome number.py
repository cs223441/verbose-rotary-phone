#palindrome number
'''
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 
Constraints:

-231 <= x <= 231 - 1

@solution
x=10
x=str(x)
print(x)
f=""
for l in range(len(x)-1,-1,-1):
    f=f+x[l]

if x==f:
    print("tue")
else:
    print("false")

'''
