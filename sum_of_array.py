n = int(input("enter the size of array: "))
arr = []
for i in range(0, n):
    ele = int(input("enter the element: "))
    arr.append(ele)
sum = 0
for i in range(0, n):
    sum = sum + arr[i]
print("sum of array is: ", sum)