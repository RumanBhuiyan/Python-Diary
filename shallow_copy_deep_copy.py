import copy

old_list = [1,2,[3,4]]
new_list = old_list
new_list[0]=100

print(f'Old list : {old_list}') #Old list : [100, 2, [3, 4]]
print(f"New list : {new_list}") #New list : [100, 2, [3, 4]]

# if we want a real copy not reference so that previous list item isn't changed
# then we need shallow copy
old_list = [1,2,[3,4]]
shallo_copied = copy.copy(old_list)
shallo_copied[0] = 0
print(f"Old list : {old_list}") #Old list : [1, 2, [3, 4]]
print(f"shallow copied list : {shallo_copied}") #shallow copied list : [0, 2, [3, 4]]   

# deep copy can prevent programmer doing nested changes both in real and copied
# object 
old_list = [1,2,[3,4]]
deep_copied = copy.deepcopy(old_list)
deep_copied[2][0] = 0
print(f"Old list : {old_list}") #Old list : [1, 2, [3, 4]]
print(f"deep copied list : {deep_copied}") #deep copied list : [1, 2, [0, 4]]