# Lock() can also be applied for multiprocessing
from  multiprocessing import Process, Lock
from time import sleep


def counter_one(array,lock,name,delay,initial):
    for i in range(initial,initial+5):
        with lock:
            array.append(i)
            print(f'from {name} Numbers : {array}')
            sleep(delay)

if __name__ == '__main__':
    numbers = []
    lock = Lock()

    process1 = Process(target=counter_one,args=(numbers,lock,'Counter 1',1,1))
    process2 = Process(target=counter_one,args=(numbers,lock,'Counter 2',2,5))

    process1.start()
    process2.start()

    process1.join()
    process2.join()