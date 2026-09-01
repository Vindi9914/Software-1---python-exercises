#print out all numbers divisible by three from 1 - 1000

num = 3
while num <= 1000:
    if num % 3 == 0:
        print(num)
    num += 1     