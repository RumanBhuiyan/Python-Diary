# handling multiple process using pool
from  multiprocessing import Process, Pool
from time import sleep

def cube(x):
    print(f'Cube of {x} is {x**3}')

# multiprocessing.cpu_count() -> informs how many CPU cores are available in this pc
if __name__ == '__main__':

    # Process : 01 (using for loop)
    processes = []
    # creating process
    for i in range(1,10):
        p = Process(target=cube,args=(i,))
        processes.append(p)

    # starting process
    for process in processes:
        process.start()
        sleep(1)


    # Process : 02 (using pool)
    all_process = Pool(2)# max_workers = 2
    all_process.map(cube,(2,3,4,5,6))


    # Process : 03 (using context manager)
    with Pool(2) as pool:
        pool.map(cube,(2,3,4,5,6))