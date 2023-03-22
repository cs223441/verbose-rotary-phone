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