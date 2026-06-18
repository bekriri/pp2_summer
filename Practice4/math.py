# math and random

import math
import random

# built in functions
nums = [3, 7, 1, 9, 4]
print("min:", min(nums))
print("max:", max(nums))
print("abs(-5):", abs(-5))
print("round(3.567, 2):", round(3.567, 2))
print("pow(2, 8):", pow(2, 8))

# math module
print("sqrt(81):", math.sqrt(81))
print("ceil(3.2):", math.ceil(3.2))
print("floor(3.9):", math.floor(3.9))
print("pi:", math.pi)
print("e:", math.e)
print("sin(90):", math.sin(math.radians(90)))
print("cos(0):", math.cos(math.radians(0)))
print("factorial(5):", math.factorial(5))

# random module
print("random:", random.random())
print("randint 1-100:", random.randint(1, 100))

colors = ["red", "green", "blue", "yellow"]
print("choice:", random.choice(colors))

random.shuffle(colors)
print("shuffle:", colors)

print("sample:", random.sample(range(1, 20), 3))
