import math
import random

uzunlik = lambda x, y : x+y
print(uzunlik(1, 2))

def daraja (x):
    return lambda y : y**x

kvadrat = daraja(2)
print(kvadrat(5))

sonlar = random.sample(list(range(1, 100)), 10)
print(sonlar)

print(list(map(lambda x:x+1, sonlar)))
print(list(filter(lambda x:x%2==1, sonlar)))


