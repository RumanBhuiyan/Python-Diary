import heapq

numbers = [1,2,3,4,5,6,7]

print(heapq.nlargest(3,numbers)) #[7, 6, 5]
print(heapq.nsmallest(3,numbers)) #[1, 2, 3]