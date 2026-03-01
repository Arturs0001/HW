def print_formatted_text():
    print("\"Don't let the noise of others' opinions")
    print("     drown out your own inner voice.\"")
    print("       Steve Jobs")


def print_odds(a, b):
    for i in range(a, b + 1):
        if i % 2 != 0:
            print(i, end=" ")
    print()


def draw_line(length, direction, symbol):
    if direction == 'h':
        for _ in range(length):
            print(symbol, end="")
        print()
    elif direction == 'v':
        for _ in range(length):
            print(symbol)
    else:
        print("errrrror")


def max_of_four(a, b, c, d):
    return max(a, b, c, d)


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_lucky(n):
    n = str(n)
    if len(n) != 6:
        return False
    s1 = int(n[0]) + int(n[1]) + int(n[2])
    s2 = int(n[3]) + int(n[4]) + int(n[5])
    if s1 == s2:
        return True
    else:
        return False




print_formatted_text()


a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
print_odds(a, b)


length = int(input("Довжина лінії: "))
direction = input("Напрямок (h / v): ")
symbol = input("Символ: ")
draw_line(length, direction, symbol)


a = int(input("Введіть 1 число: "))
b = int(input("Введіть 2 число: "))
c = int(input("Введіть 3 число: "))
d = int(input("Введіть 4 число: "))
print("Максимальне:", max_of_four(a, b, c, d))


n = int(input("Введіть число: "))
print("Просте?" , is_prime(n))


num = input("Введіть шестизначне число: ")
print(is_lucky(num))