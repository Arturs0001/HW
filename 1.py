import random
import string

def draw_header(title):
    width = 40
    print("=" * width)
    print(title.center(width))
    print("=" * width)


def draw_menu(options_list):
    for i, option in enumerate(options_list, start=1):
        print(f"[ {i} ] {option}")


def draw_warning(message):
    width = len(message) + 6
    print("!" * width)
    print(f"!!! {message} !!!")
    print("!" * width)


draw_header("ГЕНЕРАТОР НІКНЕЙМІВ")

base_name = input("Введіть базове ім'я: ").strip()

nickname1 = base_name + str(random.randint(100, 9999))

separator = random.choice(['_', '.', '-'])
letters = ''.join(random.choices(string.ascii_lowercase, k=3))
nickname2 = base_name + separator + letters

prefixes = ["Pro", "Super", "Ultra"]
prefix = random.choice(prefixes)
capitalized_name = base_name.capitalize()
digits = random.randint(10, 99)

nickname3 = prefix + capitalized_name + str(digits)

print("\nЗгенеровані нікнейми:")
print(f"1. {nickname1}")
print(f"2. {nickname2}")
print(f"3. {nickname3}")

print("\n")
draw_header("ЛАСКАВО ПРОСИМО ДО ГРИ")

menu_options = [
    "Почати гру",
    "Налаштування",
    "Вийти"
]

draw_menu(menu_options)

choice = input("\nОберіть пункт меню (1-3): ").strip()

if choice == "1":
    print("\nВи обрали: Почати гру")
elif choice == "2":
    print("\nВи обрали: Налаштування")
elif choice == "3":
    print("\nГру завершено.")
else:
    draw_warning("Некоректний пункт меню!")