
dictionary = {
    "cat": "кіт",
    "dog": "собака",
    "house": "будинок",
    "car": "автомобіль",
    "water": "вода"
}

word = input("Введіть слово англійською: ").lower()

if word in dictionary:
    print("Переклад:", dictionary[word])
else:
    print("Слово не знайдено")

print()


friends_count = int(input("Введіть кількість друзів: "))

my_games = input("Введіть свої ігри через кому: ").lower().split(",")

for i in range(friends_count):
    friend_games = input("Ігри друга " + str(i+1) + " через кому: ").lower().split(",")
    new_list = []
    for game in my_games:
        if game in friend_games:
            new_list.append(game)
    my_games = new_list

print("Ігри, в які можуть грати всі разом:")
for game in my_games:
    print(game)