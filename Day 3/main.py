import math
paths = open('paths.txt', 'r')

arr = []
for each in paths:
    arr.append(each.split()[0])

# Correct answers:
    # - Part 1: 259
    # - Part 2: 2224913600

def treeCounter(rightCount, downCount):
    right = rightCount
    total = 0

    for i in range(downCount, len(arr), downCount):
        if right > len(arr[i]) - 1:
            right -= len(arr[i])

        if arr[i][right] == '#':
            total += 1
        right += rightCount

    return total
# print(treeCounter(3, 1))
print(treeCounter(1, 1) * treeCounter(1, 2) * treeCounter(3, 1) * treeCounter(5, 1) * treeCounter(7, 1))







# ======= VERSION 2 =======

# def treeCounter(rightCount, downCount):
#     right = rightCount
#     count = 0
#     for i in range(downCount, len(arr), downCount):
#         string = '' 
#         for _ in range(math.ceil(right / (len(arr[i]) - 1 // rightCount if len(arr) % rightCount == 0 else len(arr[i]) // rightCount))):
#             string += arr[i]

#         if string[right] == '#':
#             count += 1
#         right += rightCount
#     return count

# print(treeCounter(1, 1) * treeCounter(1, 2) * treeCounter(3, 1) * treeCounter(5, 1) * treeCounter(7, 1))




#  ======= VERSION 1 =======

# rightOne = 1
# countOne = 0
# for i in range(1, len(arr)):
#     string = '' 

#     for j in range(math.ceil(rightOne / (len(arr[i]) - 1 // 1))):
#         string += arr[i]

#     if string[rightOne] == '#':
#         countOne += 1
#     rightOne += 1

# rightThree = 3
# countThree = 0
# for i in range(1, len(arr)):
#     string = '' 

#     for j in range(math.ceil(rightThree / (len(arr[i]) // 3))):
#         string += arr[i]

#     if string[rightThree] == '#':
#         countThree += 1

#     rightThree += 3

# rightFive = 5
# countFive = 0
# for i in range(1, len(arr)):
#     string = '' 

#     for j in range(math.ceil(rightFive / (len(arr[i]) // 5))):
#         string += arr[i]

#     if string[rightFive] == '#':
#         countFive += 1

#     rightFive += 5
# # print(countFive)
# rightSeven = 7
# countSeven = 0
# for i in range(1, len(arr)):
#     string = '' 

#     for j in range(math.ceil(rightSeven / (len(arr[i]) // 7))):
#         string += arr[i]

#     if string[rightSeven] == '#':
#         countSeven += 1

#     rightSeven += 7
# # print(countSeven)

# rightOneSecond = 1
# countOneSecond = 0
# for i in range(2, len(arr), 2):
#     string = '' 

#     for j in range(math.ceil(rightOneSecond / (len(arr[i]) - 1 // 1))):
#         string += arr[i]

#     if string[rightOneSecond] == '#':
#         countOneSecond += 1

#     rightOneSecond += 1
# # print(countOneSecond)

# print(countOne * countOneSecond * countThree * countFive * countSeven)