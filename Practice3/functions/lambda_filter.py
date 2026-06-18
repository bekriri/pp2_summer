# lambda with filter

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

big_numbers = list(filter(lambda x: x > 5, numbers))
print(big_numbers)

movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
]

good = list(filter(lambda m: m["imdb"] > 5.5, movies))
print("Good movies:")
for m in good:
    print(m["name"])

romance = list(filter(lambda m: m["category"] == "Romance", movies))
print("Romance:")
for m in romance:
    print(m["name"])
