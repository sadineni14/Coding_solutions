a=[100,200,300,400,500]
smallest = a[0]
for i in range(len(a)):
    if a[i] < smallest:
        smallest = a[i]
print("Smallest number in the array is:", smallest)