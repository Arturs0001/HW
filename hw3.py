number = int(input("Enter a number: "))
power = int(input("Enter power (0-7): "))

if power >= 0 and power <= 7:
    print(number ** power)
else:
    print("Error")

num = int(input("Enter number (1-100): "))

if num < 1 or num > 100:
    print("Error")
elif num % 3 == 0 and num % 5 == 0:
    print("Fizz Buzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)


print("Snack:")
print("1 - Salad ($5)")
print("2 - Soup ($7)")
snack = int(input("Choose: "))

print("Main dish:")
print("1 - Chicken ($10)")
print("2 - Fish ($12)")
main = int(input("Choose: "))

print("Dessert:")
print("1 - Ice cream ($3)")
print("2 - Fruits ($4)")
dessert = int(input("Choose: "))

regular = int(input("Regular client? "))

total = 0

if snack == 1:
    total += 5
elif snack == 2:
    total += 7
else:
    print("Error")

if main == 1:
    total += 10
elif main == 2:
    total += 12
else:
    print("Error")

if dessert == 1:
    total += 3
elif dessert == 2:
    total += 4
else:
    print("Error")

if snack == 2 and main == 2:
    total -= 2
    print("Dessert discount $2")

if main == 1 and dessert == 1:
    print("Free drink")

discount = 0.10

if total > 20:
    discount = 0.15

if regular == 1:
    discount += 0.05

final_price = total - (total * discount)

print("Final price:", final_price)
