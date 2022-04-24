import sys

odd_numbers = (1,3,5,7,9) # tuple
even_numbers = [2,4,6,8,10] # list

print(sys.getsizeof(odd_numbers)) # tuple takes 80 bytes in python3
print(sys.getsizeof(even_numbers)) # list takes 120 bytes in python3

# so in case of memory efficiency tuple is better than list but you should always keep in
# mind that tuple items are immutable whereas list items are mutable

# N.B (python2 takes less memory than python3)
# python3 size_comparison.py =>output : 80 120
# python2 size_comparison.py =>output : 48 56