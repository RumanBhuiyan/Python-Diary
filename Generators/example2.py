# example - 02
def my_range(limit):
    index = 0
    while index < limit:
        yield index
        index += 1

for num in my_range(5):
    print(num)
