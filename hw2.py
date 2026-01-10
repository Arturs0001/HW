
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

s = a + b + c
p = a * b * c

print("Sum:", s)
print("Product:", p)



d1 = float(input("Enter the first diagonal: "))
d2 = float(input("Enter the second diagonal: "))

area = (d1 * d2) / 2

print("Area of the rombus:", area)



ss = float(input("Enter monthly salary: "))
cp = float(input("Enter credit payment: "))
ud = float(input("Enter utilities debt: "))

money = ss - cp - ud

print("money:", money)



distance = float(input("Enter distance in kilometers: "))
f = float(input("Enter fuel consumption per 100 km: "))
fp = float(input("Enter fuel price per liter: "))

fuel_needed = (distance / 100) * f
trip_cost = fuel_needed * fp

print("Total trip cost:", trip_cost)



tb = float(input("Enter total restaurant bill: "))
people = float(input("Enter number of people: "))

tip = tb * 0.15
total_with_tip = tb + tip
per_person = total_with_tip / people

print("Tip amount:", tip)
print("Total with tip:", total_with_tip)
print("Amount per person:", per_person)



price_per_day = float(input("Enter rental price per day: "))
days = float(input("Enter number of rental days: "))
deposit = float(input("Enter deposit amount: "))

rental_cost = price_per_day * days
total_with_deposit = rental_cost + deposit
cost_per_day = rental_cost / days

print("Total cost including deposit:", total_with_deposit)
print("Amount to pay after returning the car:", rental_cost)
print("Cost per day:", cost_per_day)
