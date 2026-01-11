a = float(input("a = "))

if a % 2 == 0:
    print("ok")
else:
    print("ne ok")

if a % 7 == 0:
    print("ok")
else:
    print("ne ok")

b = float(input("b = "))
c = float(input("c = "))

if b > c:
    print(b)
elif b < c:
    print(c)
elif b == c:
    print("=")
else:
    print("error")

d = float(input("d = "))
e = float(input("e = "))

if d > e:
    print(e)
elif d < e:
    print(d)
elif d == e:
    print("=")
else:
    print("error")

number1 = float(input("number1 = "))
number2 = float(input("number2 = "))
operation = input("operation: ")
if operation == "+":
    print(number1 + number2)
elif operation == "-":
    print(number1 - number2)
elif operation == "*":
    print(number1 * number2)
elif operation == "C":
    print((number1 + number2)/2)
else:
    print("error")

dollar = float(input("dollar = "))
curs = float(input("curs = "))
money = input("money(Eur, Gbp, Uah  = ")
if money == "Eur":
    print(dollar * curs)
elif money == "Gbp":
    print(dollar * curs)
elif money == "Uah":
    print(dollar * curs)
else:
    print("error")