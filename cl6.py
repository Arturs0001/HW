from math import pi

sek = float(input("sek = "))
type1 = input("type(sek, m, h) = ")

if type1 == "sek":
    print(86400- sek)
elif type1 == "m":
    print(1440 - (sek / 60))
elif type1 == "h":
    print(24 - ((sek / 60) / 60))
else:
    print("error")

d = float(input("d = "))

print(pi * ((d / 2) * (d / 2)))

console_preise = float(input("console_preise = "))
count = int(input("count = "))
deal1 = int(input("deal = "))

deal2 = (console_preise / 100) * deal1

print((console_preise - deal2) * count)

bit = int(input("bit = "))
gb = float(input("gb = "))
type2 = input("type(sek, m, h) = ")
if type2 == "sek":
    print((gb * 8000000000) / bit)
elif type2 == "m":
    print(((gb * 8000000000) / bit) / 60)
elif type2 == "h":
    print((((gb * 8000000000) / bit) / 60) / 60)
else:
    print("error")


h = int(input("h = "))

if 0 <= h < 6:
    print("Good Night")
elif 6 <= h < 13:
    print("Good Morning")
elif 13 <= h < 17:
    print("Good Day")
elif 17 <= h < 24:
    print("Good Evening")
else:
    print("error")

t = float(input("t = "))

if t < -10:
    print("Дуже холодно")
elif -10 <= t < 0:
    print("Холодно")
elif 0 <= t < 15:
    print("Прохолодно")
elif 15 <= t <= 25:
    print("Тепло")
else:
    print("Спекотно")

