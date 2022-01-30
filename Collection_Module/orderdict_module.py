from collections import OrderedDict

# OrderedDict strictly maintains insertion order with all types of insertion
# updating, deleting etc python version >=3.7 dictionary can also remember
# insertion order so for python >=3.7 orderDict = dict 
keep  = OrderedDict()

keep[0] = 0
keep[1] = 1
keep[2] = 4
keep[3] = 9

print(f"Keep : {keep}")
keep[3] = 27
keep[5] = 25
print(f"Order after insertion : {keep}")

for key,value in keep.items():
    print(f"key : {key} value : {value}")
