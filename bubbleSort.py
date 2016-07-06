import random, time

arr = []

for x in range(1, 100):
	arr.append(random.randint(0, 1000))

print "Before Sort:"
print arr

start = time.time()

for x in arr:
	for i in range(0, len(arr) -1):
		if arr[i] > arr[i+1]:
			tmp = arr[i+1]
			arr[i+1] = arr[i]
			arr[i] = tmp

print "After sort:"
print arr

print "Time Elapsed:", (time.time() - start), "seconds"
 

