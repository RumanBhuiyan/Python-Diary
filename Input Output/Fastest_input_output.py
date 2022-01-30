# If C/C++ limit provided is X. then 
# Java  is 2X  time slower
# Python is 5X time slower 
# if judge sets runtime thus then your python code wont get any TLE
# but only hackerrank maintains it. codeforces,lightoj doesn't 
# that' why c++ is preferred yet stdin,stdout is preferred in python over input,print to
# get bit faster experience
from sys import stdin, stdout 

# strip removes front and back space  of the line
get_numbers = lambda : [int(x) for x in stdin.readline().strip().split() if len(x)>0] 
print_output = lambda s : stdout.write(str(s))

numbers = get_numbers()
print_output(sum(numbers))
