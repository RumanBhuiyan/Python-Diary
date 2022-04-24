# lets build our own for loop to understand iterable & iterator
# python built-in for loop works in this manner
def my_for(iterable):
    iterator = iter(iterable)
    while True :
        try :
            value = next(iterator)
        except StopIteration :
            print("Items ended")
            break
        else :
            print(value)


my_for([1,2,3,4,5])

# more than 1 item makes any object iterable so name here is iterable
name = "Ruman" 
# creating iterator so that we can iterate over name
it = iter(name)

while True :
    try :
        char = next(it)
        print(char)
    except StopIteration:
        break