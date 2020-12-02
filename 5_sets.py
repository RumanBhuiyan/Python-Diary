# Set is simmillar as Mathematical set we read in mathematics

my_friends = {'a', 'b', 'c', 'd', 'e'}
his_friends = {'c', 'd', 'f', 'g', 'h'}
# union operation
print("All friends : ", my_friends.union(his_friends))
print("All friends another way : ", my_friends | his_friends)
# intersection operation
print("Common Friends: ", my_friends.intersection(his_friends))
print("Common Friends: ", my_friends & his_friends)
# difference operation
print("They aren't my friends: ", his_friends.difference(my_friends))
print("They aren't my friends: ", his_friends - my_friends)
