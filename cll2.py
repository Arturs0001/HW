import random


nums = list(map(int, input("Введіть числа через пробіл: ").split()))
uniq = set(nums)
print("Унікальні числа:", uniq)


a = set([random.randint(1, 20) for _ in range(10)])
b = set([random.randint(1, 20) for _ in range(10)])

print("\nМножина A:", a)
print("Множина B:", b)
print("Спільні елементи:", a & b)
print("Різниця A - B:", a - b)
print("Об'єднання:", a | b)


w1 = input("\nПерше слово: ").lower()
w2 = input("Друге слово: ").lower()
set1 = set(w1)
set2 = set(w2)

if set1 == set2:
    print("Слова мають однакові множини букв (анаграми по множинах).")
else:
    print("Не збігаються множини букв.")