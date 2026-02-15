data = input("numbers for task 1: ").split()
nums = []

for x in data:
    nums.append(int(x))

total = 0
for x in nums:
    total += x

mean = total / len(nums)

print(total)
print(mean)




data = input("numbers for task 2: ").split()
nums = []

for x in data:
    nums.append(int(x))

target = int(input("number to count: "))

count = 0
for x in nums:
    if x == target:
        count += 1

print(count)




data = input("numbers for task 3: ").split()
nums = []

for x in data:
    nums.append(int(x))

positive_sum = 0
for x in nums:
    if x > 0:
        positive_sum += x

print(positive_sum)





data = input("numbers for task 4: ").split()
nums = []

for x in data:
    nums.append(int(x))

indexe = []

for i in range(len(nums)):
    if nums[i] % 2 == 0:
        indexe.append(i)

print(indexe)




data = input("numbers for task 5: ").split()
nums = []

for x in data:
    nums.append(int(x))

unique = []

for x in nums:
    if nums.count(x) == 1:
        unique.append(x)

print(unique)
