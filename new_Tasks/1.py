import math
import random


def task1():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print(a / b)
    except ValueError:
        print("Not a number")
    except ZeroDivisionError:
        print("Division by zero")
    finally:
        print("Done")


def task2():
    numbers = [10, 20, 30, 40, 50]
    try:
        index = int(input("Enter index: "))
        print(numbers[index])
    except ValueError:
        print("Not a number")
    except IndexError:
        print("Index out of range")
    finally:
        print("Done")


def task3():
    try:
        data = input("Enter numbers: ")
        nums = list(map(float, data.split()))
        print(sum(nums))
    except ValueError:
        print("Invalid input")
    finally:
        print("Done")


def task4():
    try:
        num = float(input("Enter number: "))
        if num < 0:
            raise Exception("Negative number")
        print(math.sqrt(num))
    except ValueError:
        print("Not a number")
    except Exception as e:
        print(e)
    finally:
        print("Done")


def task5():
    try:
        data = input("Enter product: ")
        name, price, quantity = data.split(",")
        price = float(price)
        quantity = int(quantity)
        print(name.strip(), price * quantity)
    except ValueError:
        print("Invalid format")
    finally:
        print("Done")


def connect_to_server():
    if random.choice([True, False]):
        return "Connected"
    else:
        raise ConnectionError("Error")


def task6():
    try:
        print(connect_to_server())
    except ConnectionError:
        print("Connection failed")
    finally:
        print("Done")


task1()
task2()
task3()
task4()
task5()
task6()