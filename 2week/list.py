import random
import statistics 
numbers = []
size = random.randint(10,15)
for _ in range(size):
	numbers.append(random.randint(1,20))
numbers.sort()
half = len(numbers) // 2
if (len(numbers) % 2):
	print (numbers[half])
else:
	print ((sum(numbers[half-1 : half +1]))/2)
print(statistics.median(numbers))