
symbol = input("Symbol: ")

width = int(input("width: "))
height = int(input("height: "))
for i in range(height):
    print(symbol * width)

figure = input("square or rectangle: ")
symbol1 = input("Symbol: ")

if figure == "square":
    side = int(input("length: "))
    for i in range(side):
        print(symbol1 * side)

elif figure == "rectangle":
    width = int(input("width: "))
    height = int(input("height: "))
    for i in range(height):
        print(symbol1 * width)

else:
    print("error")

size = int(input("size: "))

for i in range(size):
    for j in range(size):
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

width2 = int(input("width: "))
height2 = int(input("height: "))

for i in range(height2):
    for j in range(width2):
        if i == 0 or i == height2 - 1 or j == 0 or j == width2 - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


height_t = int(input("height: "))
symbol_t = input("symbol: ")

for i in range(1, height_t + 1):
    print(symbol_t * i)

height_t_1 = int(input("height: "))
symbol_t_1 = input("symbol: ")

for i in range(1, height_t_1 + 1):
    spaces = height_t_1 - i
    symbols = 2 * i - 1
    print(" " * spaces + symbol * symbols)





