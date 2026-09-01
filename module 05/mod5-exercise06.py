import random

N = int(input("How many points to generate: "))

n = 0
i = 0

while i < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 < 1:
        n = n + 1

    i = i + 1

pi = 4 * n / N

print("Approximation of pi:", pi)