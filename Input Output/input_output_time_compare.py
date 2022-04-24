from sys import stdin, stdout
import time 

# time() takes time value in seconds
start = time.time_ns()
sentence1 = [int(x) for x in input().split() if len(x)>0]
end = time.time_ns()

stdout.write(f"{end-start} nanoseconds\n")
stdout.write(f"{(end-start)/1000000000} seconds\n")

# time() takes time value in seconds
start = time.time_ns()
sentence1 = [int(x) for x in stdin.readline().split() if len(x) >0]
end = time.time_ns()


stdout.write(f"{end-start} nanoseconds\n")
stdout.write(f"{(end-start)/1000000000} seconds\n")
