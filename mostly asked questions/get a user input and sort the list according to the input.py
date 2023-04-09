'''
Q take a input from user and sort the list using the user input 
Eg:

list:a=[5,23,66,23,12,56,23,68]

Enter the number : 30

Output : [56, 66, 68, 5, 12, 23, 23, 23]

#solution
------------

new=[]
new2=[]
a=[5,23,66,23,12,56,23,68]

i=int(input("Enter the number : "))
for k in a:
    if k>=i:
        new.append(k)

new=sorted(new)

for c in a:
    if c in new:
        continue
    else:
        new2.append(c)
new2=sorted(new2)

for u in new2 :
    new.append(u)

print(f"Output : {new}")
'''