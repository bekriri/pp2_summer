# lambda with map

numbers = [1, 2, 3, 4, 5]

doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

squared = list(map(lambda x: x ** 2, numbers))
print(squared)

names = ["bekri", "aitu", "dana"]
upper = list(map(lambda n: n.upper(), names))
print(upper)

temps = [0, 20, 37, 100]
fahrenheit = list(map(lambda c: c * 9/5 + 32, temps))
print(fahrenheit)
