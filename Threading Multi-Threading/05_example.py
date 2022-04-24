# ThreadPoolExecutor module helps us to manage multiple threads
# we can run multiple threads in parallel mentioning the number in max_workers=number

from threading import Lock
from concurrent.futures import ThreadPoolExecutor
from time import sleep

counter = 0
lock = Lock()

def My_counter_withlock(name,delay):
    for _ in range(5):
        with lock:
            global counter
            counter += 1
            sleep(delay)
            print(f'from {name} Counter : {counter}')

def cube(x):
    sleep(2)
    print(f'Cube of {x} is {x**3}')

if __name__ == '__main__':
    
    # max_workers -> number of threads that will run in parallel from iterable
    # Process : 01 ThreadPoolExecutor without context manager
    myexec = ThreadPoolExecutor(max_workers=3)
    myexec.submit(cube,x=2)
    myexec.submit(cube,x=3)
    myexec.submit(cube,x=4)

    # Process : 02 ThreadPoolExecutor with context manager
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(cube,(2,3,4,5,6,7))

    counters = [('Counter 1',1),('Counter 2',2)]
    with ThreadPoolExecutor(max_workers=2) as exe:
        # process : 01
        # for counterObj in counters:
        #     exe.submit(My_counter_withlock,name=counterObj[0],delay=counterObj[1])

        #process : 02
        exe.map(lambda counter : My_counter_withlock(counter[0],counter[1]),counters)
    