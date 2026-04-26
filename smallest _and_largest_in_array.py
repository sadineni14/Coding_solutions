a = [1,2,3,4,5,6,7,8,9]
largest = a[0]
smallest = a[0]
for i in range(len(a)):
    if a[i] > largest:
        largest = a[i]
    if a[i]< smallest:
        smallest = a[i]
print("largest is:",largest)
print("smallest is:",smallest)