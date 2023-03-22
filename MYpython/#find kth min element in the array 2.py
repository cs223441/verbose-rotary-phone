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