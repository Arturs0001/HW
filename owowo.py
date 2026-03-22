def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)


def is_symmetric(lst):
    if len(lst) <= 1:
        return True
    if lst[0] != lst[-1]:
        return False
    return is_symmetric(lst[1:-1])



a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("GCD:", gcd(a, b))

num = int(input("Enter a number: "))
print("Sum of digits:", sum_digits(num))

lst_input = input("Enter numbers separated by space: ")
lst = list(map(int, lst_input.split()))

if is_symmetric(lst):
    print("The list is symmetric")
else:
    print("The list is not symmetric")