# The multiprocessing is a process in which two or more processors in computer 
# simultaneously process two or more different portion of the same program.
# we usually use this approach for CPU intensive task

# article : https://www.tutorialspoint.com/multiprocessing-in-python
# https://www.geeksforgeeks.org/multiprocessing-python-set-1/

from multiprocessing import Process

def cube(x):
    print(f'Cube of {x} is {x**3}')


if __name__ == '__main__':
    process1 = Process(target = cube,args=(2,))
    process2 = Process(target = cube,args=(3,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print('Done....')