# different types of arguments

def full_name(first, last):
    print(first + " " + last)

full_name("Bek", "Sembayev")

# default argument
def power(n, p=2):
    return n ** p

print(power(3))
print(power(2, 10))

# args example
def my_sum(*args):
    total = 0
    for i in args:
        total += i
    return total

print(my_sum(1, 2, 3, 4, 5))

# kwargs example
def show_info(**kwargs):
    for key in kwargs:
        print(key, ":", kwargs[key])

show_info(name="Bek", age=19, city="Almaty")
