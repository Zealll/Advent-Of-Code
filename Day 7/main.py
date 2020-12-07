test = open('test.txt', 'r')

arr = []
for group in test:
    arr.append(group.split())
    
# Correct Answers:
    # - Part 1: 268
    # - Part 2: 7867


# ======= Part 2 =======
tempBags = [[1, 'shiny gold']]

counter = 0
sec = 0
while tempBags:
    currBag = tempBags[0]

    for i in arr:
        firstPart = ' '.join(i[:2])
        secondPart = i[2:]

        if currBag[1] == firstPart:
            for j in range(len(secondPart)):
                if secondPart[j].isdigit():
                    counter += int(secondPart[j]) * currBag[0]
                    tempBags.append([int(secondPart[j]) * currBag[0], secondPart[j + 1] + ' ' + secondPart[j + 2]])
    tempBags.pop(0)

print(counter)



# ======= Part 1 =======
# colorsWithGold = ['shiny gold']

# while True:
#     length = len(colorsWithGold)
    
#     for i in arr:
#         firstPart = ' '.join(i[:2])
#         secondPart = ' '.join(i[2:])

#         for j in colorsWithGold:
#             if j in secondPart and firstPart not in colorsWithGold:
#                 colorsWithGold.append(firstPart)
#     if length == len(colorsWithGold):
#         break

# print(len(colorsWithGold) - 1)