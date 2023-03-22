#Revese Array
'''
o=[1,2,3,4,5,6]
for l in range(len(o)-1):
    for f in range(len(o)-1):
        if o[f]<o[f+1]:
            sw=o[f]
            o[f]=o[f+1]
            o[f+1]=sw
print(o)

'''