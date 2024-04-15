import random
numbers=[]
max=0
fddgdfgdmin=0
for i in range(0,100):
    numbers.append(random.random())
    if numbers[i]>max:
        max=numbers[i]
    if numbers[i]<min:
        min=numbers[i]
print(numbers)
print(max)
