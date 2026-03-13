def show_text():
    print('"Don\'t compare yourself with anyone in this world..."')
    print("        if you do so, you are insulting yourself.")
    print("                Bill Gates")


def even_numbers(a, b):
    for i in range(a, b + 1):
        if i % 2 == 0:
            print(i)


def draw_square(size, symbol, filled):
    for i in range(size):
        for j in range(size):
            if filled:
                print(symbol, end="")
            else:
                if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                    print(symbol, end="")
                else:
                    print(" ", end="")
        print()


def count_digits(number):
    number = abs(number)
    count = 0
    while number > 0:
        number //= 10
        count += 1
    return count


def is_palindrome(number):
    original = str(number)
    reversed_num = original[::-1]
    return original == reversed_num


show_text()
even_numbers(2, 20)
draw_square(5, "*", True)
draw_square(5, "#", False)
print(count_digits(3456))
print(is_palindrome(123321))
print(is_palindrome(421987))