#Q2.You are given two non-empty linked lists representing two non-negative integers. The digits are 
#stored in reverse order, and each of their nodes contains a single digit. Add the two numbers 
#and return the sum as a linked list.
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 243 + 564 = 807.

'''
'''
out=[]
l1 = [2,4,3]
l2 = [5,6,4]
cs= 0
if len(l1)==len(l2):
    for k in range(len(l1)):
        cs+=l1[k]
        #xc= print(cs,end="")


    print()
    cl=0
    for k in range(len(l2)):
        cl+=l2[k]
        #cc= print(cl,end="")

'''
'''
new=[]
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
if len(l1)==len(l2):
    x1 = x2 = ''
    for i in range(len(l1)):
        x1 += str(l1[i]) 
        x2 += str(l2[i])

    vv=int(x1)+ int(x2)
    vv=str(vv)
    vv=list(vv)

else:
    x1 = x2 = ''
    for i in range(len(l1)  ):
        x1 += str(l1[i]) 
    
    for e in range(len(l2)):
        x2 += str(l2[e])

    vv=int(x1)+ int(x2)
    vv=str(vv)
    vv=list(vv)

for c in range(len(vv)):
    vv[c]=int(vv[c])
    out.insert(0,vv[c])
print(f"out:{out}")
'''
