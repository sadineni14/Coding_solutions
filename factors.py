def divisors(n):
    i = 1
    while i <=n:
        if(n%i==0):
            print(i)
        i = i+1
print("Enter a number to find its factors")
divisors(int(input()))