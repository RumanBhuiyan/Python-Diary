number = int(input())

# formatting approach : 01
width = len("{0:b}".format(number))
for num in range(1,number+1):
    print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(num,width=width))

# formattig approach : 02
for num in range(1,number+1):
    width = len(f'{number:b}')
    print(f'{num:>{width}} {num:>{width}o} {num:>{width}X} {num:>{width}b}')