import random

a = random.sample(range(1, 100), 10)
b = random.sample(range(1, 100), 10)

c = [x for x in a if x in b]
print(c)