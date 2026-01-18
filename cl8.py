mark = int(input("mark ="))
if mark >= 90 and mark <= 1001:
    print("Відмінно")
elif mark <= 89 and mark >= 70:
    print("Добре")
elif mark <= 69 and mark >= 50:
    print("Задовільно")
elif mark < 50:
    print("Незадовільно")

money = int(input("money = "))
years = int(input("years = "))

pr = money / 100
if years < 1:
    print("Премія не передбачена", (pr*1)+money)
elif years > 1 and years < 3:
    print((pr*5)+money)
elif years > 3 and years < 5:
    print((pr*10)+money)
elif years > 5:
    print((pr*15)+money)

four_num = int(input("four_num = "))

a = four_num % 10
b = (four_num % 100 - four_num % 10) / 10
c = (four_num % 1000 - four_num % 100) / 100
d = (four_num  - (a+(b*10)+(c*100))) / 1000
print(a, b, c, d)

if (a + b + c + d) % 2 == 0:
    print("yes")
else:
    print("no")

six_num = int(input("six_num = "))

a1 = six_num % 10
b1 = (six_num % 100 - six_num % 10) / 10
c1 = (six_num % 1000 - six_num % 100) / 100
d1 = (six_num % 10000 - six_num % 1000) / 1000
e1 = (six_num % 100000 - six_num % 10000) / 10000
f1 = (six_num  - (a1+(b1*10)+(c1*100)+(d1*1000)+(e1*10000))) / 100000
print(a1, b1, c1, d1, e1, f1)

if (a1 + b1 +c1) == (d1 + e1 + f1):
    print("yes")
else:
    print("no")

print(a1*100000 + b1*10000 + d1*1000 + c1*100 + e1*10 + f1)