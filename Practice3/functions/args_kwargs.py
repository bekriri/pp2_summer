# args and kwargs

def print_all(*args):
    for item in args:
        print(item)

print_all("apple", "banana", "cherry")

def multiply_all(*args):
    result = 1
    for n in args:
        result = result * n
    return result

print(multiply_all(2, 3, 4))

def show_details(**kwargs):
    for k in kwargs:
        print(k + " = " + str(kwargs[k]))

show_details(name="Bek", major="CS", gpa=3.5)

# using both
def mixed(title, *args, **kwargs):
    print("Title:", title)
    print("Numbers:", args)
    print("Info:", kwargs)

mixed("Test", 1, 2, 3, city="Almaty", year=2)
