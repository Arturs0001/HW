import random

def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)


def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def days_in_month(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap(year) else 28


def date_to_days(day, month, year):
    days = day

    for y in range(1, year):
        days += 366 if is_leap(y) else 365

    for m in range(1, month):
        days += days_in_month(m, year)

    return days


def date_difference(d1, m1, y1, d2, m2, y2):
    return abs(date_to_days(d1, m1, y1) - date_to_days(d2, m2, y2))


def find_min_sequence(arr, index=0, min_index=0, min_sum=None):
    if index > len(arr) - 10:
        return min_index

    current_sum = sum(arr[index:index+10])

    if min_sum is None or current_sum < min_sum:
        return find_min_sequence(arr, index + 1, index, current_sum)
    else:
        return find_min_sequence(arr, index + 1, min_index, min_sum)


base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))
print("Result:", power(base, exp))


d1 = int(input("Day: "))
m1 = int(input("Month: "))
y1 = int(input("Year: "))

d2 = int(input("Day: "))
m2 = int(input("Month: "))
y2 = int(input("Year: "))

print("Difference in days:", date_difference(d1, m1, y1, d2, m2, y2))


arr = [random.randint(1, 100) for _ in range(100)]
print("\nGenerated list:", arr)

index = find_min_sequence(arr)
print("Starting index:", index)