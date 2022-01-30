from timeit import default_timer

large_string = ['a'] * 1000000

# process : 01
start1 = default_timer()
string1 = ''
for character in large_string:
    string1 += character
end1 = default_timer()
print(f'Process : 01 took {end1 - start1} seconds')


# process : 02
start2 = default_timer()
string2 = "".join(large_string)
end2 = default_timer()
print(f'Process : 01 took {end2 - start2} seconds')

# N.B use join() instead of + in string concatenation because its faster