



a = int(input("a = "))
b = int(input("b = "))

if a <= b:
    while a <= b:
        print(a)
        a += 1
else:
    while a >= b:
        print(a)
        a -= 1





c = int(input("c = "))
d = int(input("d = "))

if c <= d:
    while c <= d:
        if c % 2 == 1:
            print(c)
        c += 1
else:
    while c >= d:
        if c % 2 == 1:
            print(c)
        c -= 1





e = int(input("e = "))
f = int(input("f = "))

if e <= f:
    if e % 2 != 0:
        e += 1

    while e <= f:
        print(e)
        e += 2
else:
    if e % 2 != 0:
        e -= 1

    while e >= f:
        print(e)
        e -= 2





a1 = int(input("a1 = "))
b1 = int(input("b1 = "))

step = int(input("step(1 or 2) = "))

if step == 1:
    if a1 <= b1:
        while a1 <= b1:
            print(a1)
            a1 += 1
    else:
        while a1 >= b1:
            print(b1)
            b1 += 1
elif step == 2:
    if a1 <= b1:
        while a1 <= b1:
            print(b1)
            b1 -= 1
    else:
        while a1 >= b1:
            print(a1)
            a1 -= 1
else:
    print("error")




c1 = int(input("c1 = "))
d1 = int(input("d1 = "))

if c1 <= d1:
    while c1 <= d1:
        if c1 % 2 == 1:
            print(c1)
        c1 += 1
else:
    while c1 >= d1:
        if c1 % 2 == 1:
            print(d1)
        d1 += 1





a2 = int(input("a2 = "))
b2 = int(input("b2 = "))

if a2 > b2:
    temp = a2
    a2 = b2
    b2 = temp


start = a2
if start % 2 != 0:
    start += 1

while start <= b2:
    print(start)
    start += 2

start = b2
if start % 2 == 0:
    start -= 1

while start >= a2:
    print(start)
    start -= 2
