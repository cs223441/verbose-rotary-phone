#intersection: all elements that are common in both the sets
'''
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