# any(iterable) returns True if iterable has atleast one Truthy item
# all(iterable) returns True if all items are Truthy
numbers = [1,2,3,4,5]

print(any(numbers)) # True
print(all(numbers)) # True

keep = [ num for num in range(0,4,1)]

# any can check if any item satisfies a certain condition
realNumbers = [-2,-1,10]
print(any([ num for num in realNumbers if num>0])) # True

# all can check if all items satisfy a certain condition
realNumbers = [-2,-1,-10]
print(all([ num for num in realNumbers if num<0])) # True

# reducing redundant or and at the time of combining logic using any, all

day = 'sunday'
time = '5.00PM'
money = 500

if day == 'sunday' and time == '5.00PM' and money >= 500:
    print('I will buy the book definitely')

# lets refactor the logic above 
if all([day == 'sunday', time == '5.00PM', money >= 500]):
    print('I will buy the book definitely')

if day == 'sunday' or time == '5.00PM' or money >= 500:
    print('I may buy the book. There is a possibility but not sure')

# lets refactor the logic above
if any([day == 'sunday', time == '5.00PM', money >= 500]):
    print('I may buy the book. There is a possibility but not sure')