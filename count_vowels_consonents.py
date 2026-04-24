n = input("enter a string: ")
vowels = 0
consonents = 0
x = len(n)
for i in range(0,x):
    if n[i] == 'a' or n[i] == 'e' or n[i] == 'i' or n[i] == 'o' or n[i] == 'u' or n[i] == 'A' or n[i] == 'E' or n[i] == 'I' or n[i] == 'O' or n[i] == 'U':
        vowels = vowels + 1
    else:
        consonents = consonents + 1
print("vowels:", vowels)
print("consonents:", consonents)
