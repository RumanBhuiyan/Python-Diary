def get_next_even_number(initial=0, limit=0):
    # decrease initial by 2 if even as its value will be increase inside while loop for first time
    initial -= 2 if initial %2 == 0 else 0 

    while True:
        # add 2 to get next even number if current number is even otherwise add 1 to get next even number from current odd number
        initial += 2 if initial %2 == 0 else 1
        if initial > limit:
            break
        yield initial

print(get_next_even_number(2,21))
print(list(get_next_even_number(2,21)))

for even_number in get_next_even_number(2, 21):
    print(even_number)
