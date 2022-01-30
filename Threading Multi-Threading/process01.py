# A program in execution is known as a process.When you start any app or program on your computer such as the internet browser, the operating system treats it like a process.
# A process may consist of several threads of execution that may execute concurrently.

# Multithreading in Python is a popular technique which enables multiple tasks to be executed at the same time. In simple words, the ability of a processor to execute multiple threads simultaneously is known as multithreading.

# The ability of a processor to execute several unrelated processes simultaneously is known as multiprocessing. These processes do not share any resources.

# race conditions happen when two or more threads access the shared piece of data and resource.

# article resource:
# https://www.analyticsvidhya.com/blog/2021/04/beginners-guide-to-threading-in-python/
# https://www.simplifiedpython.net/python-threading-example/
# https://www.datacamp.com/community/tutorials/threading-in-python
# https://www.scaler.com/topics/multithreading-in-python/
# https://www.guru99.com/python-multithreading-gil-example.html

import threading
import time


def counter(name,delay):
    print(f'{name} thread starts...')
    for i in range(1,6):
        print(f'{name} : {i}')
        i += 1
        time.sleep(delay)
    print(f'{name} thread ended')


def main():
    print('Main thread starts...')

    # this approach will run two counter synchronously
    # counter('Counter 1',1)
    # counter('Counter 2',2)

    counter1 = threading.Thread(target = counter, args =('Counter 1',1))
    counter2 = threading.Thread(target = counter, args =('Counter 2',2))

    # start() will call the run() method of Thread object counter1.run() and counter2.run()
    counter1.start()
    counter2.start()

    # join() waits for finishing the thread and wont let print 'Main thread ended'
    # before the thread finishes
    # counter1.join()
    # counter2.join()

    print('Main thread ended...')


if __name__ == '__main__':
    main()