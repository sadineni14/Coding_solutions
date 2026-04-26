a = [1,2,3,4,5,100]
max_element = a[0]
for i in range(len(a)):
    if a[i] > max_element:
        max_element = a[i]
print(max_element)