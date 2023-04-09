
#Q. given a matrix tell the which row and collumn has the highest value of sum 

#solution
a=[ [1,323,17],
    [2,4,12],
    [5,2,125], 
    [3,5,73]]

c=[[0,0,0,0],
   [0,0,0,0],
   [0,0,0,0]]  
for k in range(len(a)):
    for v in range(len(a[0])):
        c[v][k] = a[k][v]

sd=[]

for k in range(len(c)):
    s=sum(c[k])
    sd.append(s)

mx=max(sd)

if sd.count(mx)>1:
    print("there's no maximum value")
    exit()
else:
    for v in range(len(c)):
        if sum(c[v])==mx:
            print(f"{v+1} column has maximum sum")

sm_ln=len(a[0])
big_ln=len(a)


for k in range(len(a)):
    s=sum(a[k])
    sd.append(s)

mx=max(sd)

if sd.count(mx)>1:
    print("there's no maximum value")
    exit()
else:
    for v in range(len(a)):
        if sum(a[v])==mx:
            print(f"{v+1} row has maximum sum")