import math
a = [100, 200, 300, 400, 500]
first = math.inf
second = math.inf
for i in range(0,len(a)):
    if a[i] < first:
        first = a[i]
    elif a[i] < second and a[i] != first:
        second = a[i]
print("Second smallest number in the array is:", second)        