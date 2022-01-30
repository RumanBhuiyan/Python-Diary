# communication within Processes are done in 2 ways
# i)  Queue (discussed in step 03)
# ii) Pipe  (discussed in step 04)
import multiprocessing
import time

lock = multiprocessing.Lock()

def counter(initial,shared_queue):
    for i in range(initial,initial+5):
        shared_queue.put(i)
        print(f'{i} kept in queue')
        time.sleep(1)

if __name__ == '__main__':

    shared_numbers = multiprocessing.Queue()

    process1 = multiprocessing.Process(target=counter,args=(1,shared_numbers))
    process1.start()
    process1.join()

    # accessing queue items
    while shared_numbers:
        if shared_numbers.empty():
            break
        print(shared_numbers.get())


