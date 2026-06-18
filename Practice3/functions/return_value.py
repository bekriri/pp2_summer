# return values in functions

def multiply(a, b):
    return a * b

print(multiply(4, 5))

def get_min_max(lst):
    return min(lst), max(lst)

low, high = get_min_max([3, 7, 1, 9, 4])
print("min:", low)
print("max:", high)

def check_pass(score):
    if score >= 50:
        return "passed"
    return "failed"

print(check_pass(75))
print(check_pass(30))

def make_list(n):
    result = []
    for i in range(n):
        result.append(i * 2)
    return result

print(make_list(5))
