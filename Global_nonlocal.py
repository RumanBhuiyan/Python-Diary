# global keyword refers to global variable
counter = 0

def increment():
    global counter
    counter +=1
    return counter

#print(increment())

# nonlocal keyword access parents value
def myfunc1():
  x = "John"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())

