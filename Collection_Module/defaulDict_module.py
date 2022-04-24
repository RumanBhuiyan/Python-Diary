from collections import defaultdict

# if you try to access a key which doesn't exist in dictionary that
# throws KeyError but in defaultdict it wont show error rather returns 0
# it means non existing key will be initialized by an integer which is 0
# you can use others like float string
keep  = defaultdict(int)
keep[0] = 0
keep[1] = 1
keep[2] = 4
keep[3] = 9

print(keep[2])
print(keep[5]) # now keep = [0:0,1:1,2:4,3:9,5:0]

# to know more details about defaultdict functions use help(keep)