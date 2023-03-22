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