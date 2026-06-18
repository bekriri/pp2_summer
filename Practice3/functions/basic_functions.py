# basic functions examples

def say_hello():
    print("Hello!")

say_hello()

def greet(name):
    print("Hello " + name)

greet("Bekri")

def add_numbers(a, b):
    return a + b

result = add_numbers(10, 5)
print(result)

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

print(is_even(4))
print(is_even(7))
