# communication within Processes are done in 2 ways
# i)  Queue (discussed in 03_example)
# ii) Pipe  (discussed in 04_example)

from multiprocessing import Process, Queue, Lock
from time import sleep

lock = Lock()

def counter(initial,shared_queue):
    for i in range(initial,initial+5):
        shared_queue.put(i)
        print(f'{i} kept in queue')
        sleep(1)

if __name__ == '__main__':

    shared_numbers = Queue()

    process1 = Process(target=counter,args=(1,shared_numbers))
    process1.start()
    process1.join()

    # accessing queue items
    while shared_numbers:
        if shared_numbers.empty():
            break
        print(shared_numbers.get())


