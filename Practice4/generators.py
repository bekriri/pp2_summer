# iterators and generators

# iter and next
my_list = [10, 20, 30, 40]
it = iter(my_list)
print(next(it))
print(next(it))
print(next(it))

# loop through iterator
fruits = iter(["apple", "banana", "cherry"])
for f in fruits:
    print(f)

# custom iterator
class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        val = self.current
        self.current += 1
        return val

for n in Counter(1, 5):
    print(n)

# generator with yield
def even_gen(limit):
    n = 0
    while n <= limit:
        yield n
        n += 2

for num in even_gen(10):
    print(num)

# fibonacci generator
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(7):
    print(num, end=" ")
print()

# generator expression
squares = (x * x for x in range(1, 6))
for s in squares:
    print(s, end=" ")
print()
