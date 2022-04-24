from itertools import accumulate
import operator

# accumulate iterate all items of a list and performs a common operation
# over them by defual operation is addition.but we can specify operation like below
a = [1,2,3]
acc1 = accumulate(a)
acc2 = accumulate(a,func=operator.mul)
acc3 = accumulate(a,func=max)

print(a) #[1, 2, 3]
print(list(acc1)) #[1, 3, 6]
print(list(acc2)) #[1, 2, 6]
print(list(acc3))