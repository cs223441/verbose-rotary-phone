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