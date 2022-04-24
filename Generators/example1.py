# example - 01
def get_number():
    x = 1
    yield x

    x += 2
    yield x

    x += 3
    yield x


# process -01 : accessing value where StopIteration is catched and handled by for loop
for num in get_number():
    print(num)


# Process -02 : where we will catch StopIteration and handle it in our own way
iterator = get_number()
while True:
    try :
        value = next(iterator)
    except StopIteration:
        break
    else:
        print(value)