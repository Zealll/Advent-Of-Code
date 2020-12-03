# ===== Part 1 Starts here =====
# ***Find the two entries that sum to 2020; what do you get if you multiply them together?
arr = []

nums = open('nums.txt', 'r')
for num in nums:
    arr.append(int(num))

for i in arr:
    if 2020 - i in arr:
        print(i, 2020 - i, (2020 - i) * i)

# ===== Part 1 Ends here =====

# ===== Part 2 Starts here =====
# ***What is the product of the three entries that sum to 2020?
arr.sort()

for i in range(0, len(arr) - 2):
    vector1 = i + 1
    vector2 = len(arr) - 1

    while vector1 < vector2:
        sum = arr[i] + arr[vector1] + arr[vector2]
        if sum == 2020:
            print(arr[i], arr[vector1], arr[vector2], arr[i] * arr[vector1] * arr[vector2])
            break
        elif sum < 2020:
            vector1 += 1
        elif sum > 2020:
            vector2 -= 1