# implementing thread using class bassed approach inheriting threading.Thread class
import threading
from process01 import counter


class My_counter(threading.Thread):
    def __init__(self,name,delay):
        threading.Thread.__init__(self)
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