test = open('test.txt', 'r')

arr = []
for group in test:
    arr.append(group.split())
    
# Correct Answers:
    # - Part 1: 268
    # - Part 2: 

colorsWithGold = ['shiny gold']

while True:
    length = len(colorsWithGold)
    
    for i in arr:
        firstPart = ' '.join(i[:2])
        secondPart = ' '.join(i[2:])

        for j in colorsWithGold:
            if j in secondPart and firstPart not in colorsWithGold:
                colorsWithGold.append(firstPart)
    if length == len(colorsWithGold):
        break

print(len(colorsWithGold) - 1)
# combinedGroups = [[]]
# for i in arr:
#     if len(i) == 0:
#         combinedGroups.append(i)
#     else:
#         combinedGroups[len(combinedGroups) - 1] += i








