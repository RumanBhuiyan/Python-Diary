# implementing thread using class bassed approach inheriting threading.Thread class

from threading import Thread
from time import sleep

def counter(name,delay):
    print(f'{name} thread starts...')
    for i in range(1,6):
        print(f'{name} : {i}')
        i += 1
        sleep(delay)
    print(f'{name} thread ended')


class My_counter(Thread):
    def __init__(self,name,delay):
        Thread.__init__(self)
        self.name = name
        self.delay = delay
    
    def run(self):
        counter(self.name,self.delay)


def main():
    print('Main thread starts....')

    counter1 = My_counter('Counter 1',1)
    counter2 = My_counter('Counter 2',1)

    counter1.start()
    counter2.start()

    counter1.join()
    counter2.join()

    print('Main thread ends...')

if __name__ == '__main__':
    main()