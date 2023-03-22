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
#solution

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
