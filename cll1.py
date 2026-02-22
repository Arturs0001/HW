
contacts = {
    'Антон': '0506959068',
    'Ліза': '0474838458',
    'Сергій': '0550404033'
}

while True:
    print("\n1-Додати контакт 2-Видалити контакт 3-Змінити контакт 4-Відобразити всі контакти 5-Вихід")
    choice = input("Виберіть дію: ").strip()

    if choice == '1':
        name = input("Ім'я: ").strip()
        phone = input("Телефон: ").strip()
        contacts[name] = phone
        print("Додано.")

    elif choice == '2':
        name = input("Ім'я для видалення: ").strip()
        if name in contacts:
            contacts.pop(name)
            print("Видалено.")
        else:
            print("Не знайдено.")

    elif choice == '3':
        name = input("Ім'я для зміни: ").strip()
        if name in contacts:
            new_phone = input("Новий телефон: ").strip()
            contacts[name] = new_phone
            print("Змінено.")
        else:
            print("Не знайдено.")

    elif choice == '4':
        if contacts:
            print("Список контактів:")
            for k in contacts:
                print(f"{k}: {contacts[k]}")
        else:
            print("Контакти порожні.")

    elif choice == '5':
        break

    else:
        print("Невірний вибір.")



text = input("\nВведіть текст: ").lower()
words = text.split()
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
print("Підрахунок слів:")
for w in counts:
    print(w, counts[w])



rates = {"USD": 40.2, "EUR": 42.5, "PLN": 9.6}
uah = float(input("\nСума у гривнях: "))
cur = input("Введіть валюту (USD/EUR/PLN): ").upper()

if cur in rates:
    print(f"{uah} UAH = {uah / rates[cur]} {cur}")
else:
    print("Валюта не знайдена.")



translator = {"apple":"яблуко","book":"книга","cat":"кіт","water":"вода"}
w = input("\nВведіть англійське слово: ").strip().lower()
if w in translator:
    print(translator[w])
else:
    print("Слово не знайдено.")