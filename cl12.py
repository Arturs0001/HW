a = int(input())

for i in range(11):
    print(a * i)

for i in range(11):
    print(i * 1)
    print(i * 2)
    print(i * 3)
    print(i * 4)
    print(i * 5)
    print(i * 6)
    print(i * 7)
    print(i * 8)
    print(i * 9)
    print(i * 10)



N = int(input("N: "))


max_number = float(input("num 1: "))

for i in range(1, N):
    number = float(input(f"num : "))
    if number > max_number:
        max_number = number

print("Max_Num:", max_number)

import random
number1 = random.randint(1, 500)


while True:
    number2 = int(input("From 1 to 500: "))
    if number1 > number2:
        print("number1 > number2")
        continue
    elif number1 < number2:
        print("number1 < number2")
        continue
    else :
        print("Win")
        print(number1)
        break

figure = input("square or rectangle: ")
symbol = input("Symbol: ")

if figure == "square":
    side = int(input("length: "))
    for i in range(side):
        print(symbol * side)

elif figure == "rectangle":
    width = int(input("width: "))
    height = int(input("height: "))
    for i in range(height):
        print(symbol * width)

else:
    print("error")
