armstrong_num = []

print("Generating Armstrong numbers, please wait...")

for i in range(1, 10**7): #You can adjust the range to your own needs
    numbers = list(map(int, str(i)))
    n = len(numbers)
    s = sum(c**n for c in numbers)
    
    if s == i:
        armstrong_num.append(i)

print("Here are the Armstrong numbers:", armstrong_num)
