# when multiple threads share same resource then if any thread changes the value of that
# resource without preventing other threads to access this resource then other threads got
# unexpected result from that resource.Thats why lock came to rescue. When any thread 
# will change resource then at first it will lock it by acquire() after doing it own task
# it will unlock the resource by release() so that other threads can get access also.
import threading
import time

counter = 0
lock = threading.Lock() # assigning reference of Lock() to local variable lock

def my_counter(name,delay):
    print(f'{name} thread starts...')

    for _ in range(5):
        global counter # global variable counter
        lock.acquire() # lock the access of global variable value counter
        counter += 1
        print(f'{name} increased counter : {counter}')
        lock.release() # unlock the access of global variable value counter
        time.sleep(delay)

    print(f'{name} thread ended...')

if __name__ == '__main__':
    print(f'Global counter : {counter}')

    counter1 = threading.Thread(target=my_counter,args=('Counter 1',1))
    counter2 = threading.Thread(target=my_counter,args=('Counter 2',2))

    counter1.start()
    counter2.start()

    print('Main Thread ended...')