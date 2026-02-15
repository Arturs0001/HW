

start = int(input("Start: "))
end = int(input("End: "))

i = start
while i <= end:
    if i % 7 == 0:
        print(i, end=' ')
    i += 1
print()




start = int(input("Start: "))
end = int(input("End: "))

i = start
while i <= end:
    print(i, end=' ')
    i += 1
print()

i = end
while i >= start:
    print(i, end=' ')
    i -= 1
print()

i = start
count5 = 0
while i <= end:
    if i % 7 == 0:
        print(i, end=' ')
    if i % 5 == 0:
        count5 += 1
    i += 1
print()
print(count5)




start = int(input("Start: "))
end = int(input("End: "))

i = start
while i <= end:
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz", end=' ')
    elif i % 3 == 0:
        print("Fizz", end=' ')
    elif i % 5 == 0:
        print("Buzz", end=' ')
    else:
        print(i, end=' ')
    i += 1
print()




start = int(input("Start: "))
end = int(input("End: "))
step = int(input("Step: "))
order = input("Order (f / r): ")

if order == 'f':
    i = start
    while i <= end:
        print(i, end=' ')
        i += step
else:
    i = end
    while i >= start:
        print(i, end=' ')
        i -= step
print()




start = int(input("Start: "))
end = int(input("End: "))

if start > end:
    start, end = end, start

i = start
product = 1
found = False

while i <= end:
    if i % 4 == 0 and i % 6 != 0:
        product *= i
        found = True
    i += 1

if found:
    print(product)
else:
    print("No numbers")




A = int(input("A: "))
N = int(input("N: "))

result = 1
i = 0

while i < N:
    result *= A
    i += 1

print(result)
