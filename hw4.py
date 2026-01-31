a = int(input("num: "))
b = int(input("num: "))
c = int(input("num: "))
x = int(input("1-sum 2-mul: "))

if x == 1:
    print("result:", a + b + c)
elif x == 2:
    print("result:", a * b * c)

a = int(input("num: "))
b = int(input("num: "))
c = int(input("num: "))
x = int(input("1-max 2-min 3-avg: "))

if x == 1:
    if a >= b and a >= c:
        print("max:", a)
    elif b >= a and b >= c:
        print("max:", b)
    else:
        print("max:", c)
elif x == 2:
    if a <= b and a <= c:
        print("min:", a)
    elif b <= a and b <= c:
        print("min:", b)
    else:
        print("min:", c)
elif x == 3:
    print("avg:", (a + b + c) / 3)

g = int(input("grade: "))

match g:
    case 1:
        print("very bad")
    case 2:
        print("bad")
    case 3:
        print("ok")
    case 4:
        print("good")
    case 5:
        print("excellent")

m = float(input("meters: "))
x = int(input("1-one 2-all 3-km+cm: "))

if x == 1:
    y = int(input("1-mile 2-inch 3-yard: "))
    if y == 1:
        print("miles:", m / 1609.34)
    elif y == 2:
        print("inches:", m * 39.37)
    elif y == 3:
        print("yards:", m * 1.094)
elif x == 2:
    print("miles:", m / 1609.34)
    print("inches:", m * 39.37)
    print("yards:", m * 1.094)
elif x == 3:
    print("km:", m / 1000)
    print("cm:", m * 100)

a = float(input("num: "))
b = float(input("num: "))
x = int(input("1+ 2- 3* 4/ 5% 6^: "))

match x:
    case 1:
        print("res:", a + b)
    case 2:
        print("res:", a - b)
    case 3:
        print("res:", a * b)
    case 4:
        if b != 0:
            print("res:", a / b)
    case 5:
        print("res:", a % b)
    case 6:
        print("res:", a ** b)

n = int(input("num: "))

d1 = n // 100
d2 = (n // 10) % 10
d3 = n % 10

if d1 == d2 == d3:
    print("same digits")
else:
    print("different digits")
