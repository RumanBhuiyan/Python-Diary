import pdb

first = 3
second = 5
pdb.set_trace()

summation  = first + second
product = first * second

print(f'Summation is {summation}') 
print(f'product is {product}') 

# when you  run your program then pdb shell get opened in terminal
# type l -> list of lines in program & mark the current line with arrow
# type n -> tell to execute next line
# type c -> execute rest of lines 
# type p variable_name -> print value of a variable
