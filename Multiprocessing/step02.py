# handling multiple process using pool
import multiprocessing
from step01 import cube
import time

# multiprocessing.cpu_count() -> informs how many CPU cores are available in this pc
if __name__ == '__main__':

    # Process : 01 (using for loop)
    #processes = []
    #creating process
    # for i in range(1,10):
    #     p = multiprocessing.Process(target=cube,args=(i,))
    #     processes.append(p)

    # starting process
    # for process in processes:
    #     process.start()
    #     time.sleep(1)


    # Process : 02 (using pool)
    # all_process = multiprocessing.Pool(2)# max_workers = 2
    # all_process.map(cube,(2,3,4,5,6))


    # Process : 03 (using context manager)
    with multiprocessing.Pool(2) as pool:
        pool.map(cube,(2,3,4,5,6))