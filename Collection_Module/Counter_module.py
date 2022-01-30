from collections import Counter

name = "madam"
# make a dictionary where key is  each letter in name iterable and
# value is the number of occurance of that letter in the iterable
letter_frequency = Counter(name)

print(letter_frequency)
# shows that items first which has higher frequency
print(f"most common : {letter_frequency.most_common()}")
# decrease the frequency of 'd' by 1 
letter_frequency.subtract({'d':1}) 
print(f"After subtraction: {letter_frequency}")

letter_frequency.update({'d':2})
print(f"After updating: {letter_frequency}")

# there are lot of built-in functions  for Counter class 
# you can find them in help(Counter) or in intellisense after hitting .
