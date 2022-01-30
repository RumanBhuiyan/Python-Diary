#https://www.geeksforgeeks.org/python-itertools/
import itertools

list1 = [1,3,5,7]
list2 = [2,4,6,8]

# chain(iterable1,iterable2) -> returns an iterable object
# chain method combines two iterables
print(f'Chaining iterables : {list(itertools.chain(list1,list2))}')
list3 = [list1,list2] # from_iterables will convert list of list to single list
print(f'Chaining from_iterable : {list(itertools.chain.from_iterable(list3))}')

# compress(iterable1,boolean_iterable2) -> returns an iterable object
#compress() select values from first argument basis on boolean values on second argument
vowels = list(itertools.compress("ABCDEFGHI",[1,0,0,0,1,0,0,0,1]))
print(f'Compress {vowels}')

# dropwhile(lambda function of condition,iterable1) -> returns an iterable object
# dropwhile returns rest items of iterable when a certain condition becomes false
greater_than_four = list(itertools.dropwhile(lambda x : x <=4,list2))
print(f'Greater than four {greater_than_four}')

# takewhile(lambda function of condition,iterable1) -> returns an iterable object
# takewhile returns all items before when condition becomes false for first time
less_than_four = list(itertools.takewhile(lambda x : x <4,list2))
print(f'Less than four {less_than_four}')

# filterfalse(lambda function of condtion,iterable1) -> returns an iterable object
# filterfalse returns all iterm of iterable which didn't pass the condition
list3 = list(itertools.chain.from_iterable(list3))
odd_numbers = list(itertools.filterfalse(lambda x : x %2 ==0 , list3))
print(f'Odd numbers are {odd_numbers}')

#islice(iterable,star_index,stop_index,step) -> returns a slice
print(f'Slice : {list(itertools.islice(list3,1,6,2))}')