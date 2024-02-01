import random

# Zufällige Gleitkommazahl zwischen 0 und 1
print(f"Random Randrange:", random.randrange(13, 19))
random_float = random.random()
print(f"Zufällige Gleitkommazahl zwischen 0 und 1:", random_float)
print(f"Random Triangle:", random.triangular(20, 60, 30))
mylist = ["apple", "banana", "cherry"]

print(f"Random choice:", random.choice(mylist))
print(f"Random Sample:", random.sample(mylist, k=2))