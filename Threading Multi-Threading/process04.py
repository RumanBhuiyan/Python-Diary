# we can use lock as context manager like below. Then we don't need to manually 
# acquire() and release() rather context manger does it automatically for us
import threading
import time


counter = 0
lock = threading.Lock()


def My_counter_withoutlock(name,delay):
    for _ in range(5):
        global counter
        counter += 1
        time.sleep(delay)
        print(f'from {name} Counter : {counter}')


def My_counter_withlock(name,delay):
    for _ in range(5):
        with lock:
            global counter
            counter += 1
            time.sleep(delay)
            print(f'from {name} Counter : {counter}')

if __name__ == '__main__':
    counter1 = threading.Thread(target = My_counter_withoutlock,args=('Counter 1',1))
    counter2 = threading.Thread(target = My_counter_withoutlock,args=('Counter 2',2))


    print("Without lock.....")
    counter1.start()
    counter2.start()

    counter1.join()
    counter2.join()

    counter3 = threading.Thread(target = My_counter_withlock,args=('Counter 3',1))
    counter4 = threading.Thread(target = My_counter_withlock,args=('Counter 4',2))


    print('With lock...')
    counter3.start()
    counter4.start()