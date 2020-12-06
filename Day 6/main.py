testGroup = open('testGroup.txt', 'r')

arr = []
for group in testGroup:
    arr.append(group.split())

combinedGroups = [[]]
for i in arr:
    if len(i) == 0:
        combinedGroups.append(i)
    else:
        combinedGroups[len(combinedGroups) - 1] += i

# Correct Answers:
    # - Part 1: 6504
    # - Part 2: 3351


# ======= Part 2 =======
total = 0
for i in combinedGroups:
    if len(i) == 1:
        letters = ''
        for letter in range(len(i[0])):
            if i[0][letter] not in letters:
                letters += i[0][letter]
        total += len(letters)
    else:
        exampleString = [i[0]]
        for group in range(1, len(i)):
            exampleString.append([])
            for letter in i[group]:
                if letter in exampleString[len(exampleString) - 2] and letter not in exampleString[len(exampleString) - 1]:
                        exampleString[len(exampleString) - 1].append(letter)

        total += len(exampleString[len(exampleString) - 1])

print(total)


# ======= Part 1 =======
# total = 0
# for i in combinedGroups:
#     fullString = ''.join(i)
#     answered = []
#     for letter in fullString:
#         if letter not in answered:
#             answered.append(letter)
#     total += len(answered)

# print(total)
