# lambda with sorted

numbers = [5, 2, 8, 1, 9, 3]
print(sorted(numbers))
print(sorted(numbers, reverse=True))

words = ["banana", "apple", "kiwi", "fig"]
by_len = sorted(words, key=lambda w: len(w))
print(by_len)

movies = [
    {"name": "Usual Suspects", "imdb": 7.0},
    {"name": "Dark Knight", "imdb": 9.0},
    {"name": "Bride Wars", "imdb": 5.4},
    {"name": "The Help", "imdb": 8.0},
]

by_score = sorted(movies, key=lambda m: m["imdb"], reverse=True)
print("by imdb score:")
for m in by_score:
    print(m["name"], "-", m["imdb"])

by_name = sorted(movies, key=lambda m: m["name"])
print("alphabetical:")
for m in by_name:
    print(m["name"])
