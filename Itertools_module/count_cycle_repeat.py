from itertools import count , cycle ,repeat

# Python provides three types of infinite iterators : 
# repeat(value,how_many_times_to_repeat) ; second argument is optional 
# count(starting_value,step) ; step default value is 1
# cycle (iterable) ; iterate infinitely over this

# repeate 4 times
for i in repeat(1,5):
    print(i)
# for i in repeat(1) :  will work as an infinite loop


# start i = 1 and increment i +=2 
for i in count(1,2):
    if i > 10:
        break
    print(f'{i}th odd number : {i}')

# using counter we're controlling cycle for 2 times 
a = [1,2,3]
counter = 0
for number in cycle(a):
    print(number)
    if number == 3 :
        counter += 1
    if counter == 2:
        break
