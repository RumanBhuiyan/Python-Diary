# Pipe is used to maintain communication within processes 
# Pipe() returns two connection one who listens from left & other who listens from right
# side of the pipe. send() is used to inform something & recv() is used to accept

from multiprocessing import Process,Pipe

def print_squares(numbers,connection):
    for num in numbers:
        print(f'Square of {num} is {num**2}')

    connection.send('Square function finished')
    print(connection.recv())


def print_cubes(numbers,connection):
    for num in numbers:
        print(f'Cube of {num} is {num**3}')
        
    connection.send('Cube function finished')
    print(connection.recv())

if __name__ == '__main__':
    numbers = [1,2,3,4,5]
    left , right = Pipe()

    process1 = Process(target = print_squares,args=(numbers,left))
    process2 = Process(target = print_cubes,args=(numbers,right))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    