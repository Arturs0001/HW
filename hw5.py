import random

nums = list(map(int, input().split()))
n = int(input())
n %= len(nums)
print(nums[-n:] + nums[:-n])

a = []
for i in range(10):
    a.append(random.randint(1, 20))

b = []
for i in range(10):
    b.append(random.randint(1, 20))

print(a)
print(b)
print(a + b)
print(list(set(a + b)))
print(list(set(a) & set(b)))
print(list(set(a) ^ set(b)))
print([min(a), max(a), min(b), max(b)])