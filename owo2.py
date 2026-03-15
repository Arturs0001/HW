try:

    num1 = float(input("Enter a praise: "))
    num2 = float(input("Enter %: "))

    final_num = num1 - (num1 * num2 / 100)
    print(final_num)

except ValueError:
    print("Please enter a number!")


try:
    value = float(input("Enter a praise: "))
    rate = float(input("Enter a rate: "))

    if rate == 0:
        raise Exception("Rate cant't be zero!")

    euro = value * rate

    print(euro)

except ValueError:
    print("Please enter a number!")
except Exception as e:
    print("Error<:", e)

finally:
    print("завершення операції")



try:
    grades_input = input("Enter a grades: ")
    grades = list(map(float, grades_input.split()))

    average = sum(grades) / len(grades)
    print("Average grades:", average)

except ValueError:
    print("Please enter a number!")
except ZeroDivisionError:
    print("Can't divide by zero!")

finally:
    print(".")

balance = 1000

try:
    amount = int(input("Enter a amount: "))

    if amount % 10 != 0 or amount > balance:
        raise Exception("Incorrect amount!")

    balance -= amount
    print("New Balance:", balance)

except ValueError:
    print("Please enter a number!")
except Exception as e:
    print("Error:", e)

finally:
    print(".")

try:
    order = input("Enter a ord-num pls <3: ")

    if order[:3] != "ORD":
        raise Exception("Неправильний формат номера замовлення")

    print("Correct num")

except Exception as e:
    print("Error:", e)
finally:
    print(".")

try:
    numbers_input = input("Enter a split numbers: ")
    numbers_str = numbers_input.split()

    numbers = []

    for n in numbers_str:
        try:
            numbers.append(float(n))
        except ValueError:
            print("WARNING: incorect numbers:", n)

    total = sum(numbers)
    average = total / len(numbers)

    print("Sum:", total)
    print("Average:", average)

except ZeroDivisionError:
    print("nO CORRECT numbers!")
finally:
    print(".")


