'''
2.(Find Union and Intersection of two unsorted arrays)
#Given two unsorted arrays that represent two sets (elements in every array are distinct), find the union and intersection of two arrays.
Example: 

arr1[] = {7, 1, 5, 2, 3, 6} 
arr2[] = {3, 8, 6, 20, 7} 
Then your program should print Union as {1, 2, 3, 5, 6, 7, 8, 20} and Intersection as {3, 6, 7}. Note that the elements of union and intersection can be printed in any order.


#definition of union :  all elements that found in both sets but should not repeat

@solution
-------------
new=[]
set1=[1,4,5,7,3,23]
set2=[4,32,4,6,734,7,78,3]
for l in range(len(set1)):
    if set1[l] in set2:
        continue
    else:
        set2.append(set1[l])
for c in range(len(set2)):
    if set2[c] in new:
        continue
    else:
        new.append(set2[c])
new=sorted(new)
print(f"set1:{set1}")
print(f"set2:{set2}")
print(f"Union of set1 and set2 is : {new}")
'''