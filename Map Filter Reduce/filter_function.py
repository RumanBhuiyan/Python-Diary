# inside filter  function as argument 
# we provide a function and an iterable object like list tuple set dictionary.
#  filter function keeps those items to left_side variable who pass the condition
#  of lambda function
def get_even_numbers(x):
    return True if x%2 == 0 else False

numbers = [1,2,3,4,5,6]

even_numbers = filter(get_even_numbers,numbers)
odd_numbers = filter(lambda x : x%2 !=0,numbers)

def print_items(numbers):
    for num in numbers :
        print(num,end=' ')

print("Even numbers : ",end=" ")
print_items(even_numbers)
print("\nOdd numbers : ",end=" ")
print_items(odd_numbers)