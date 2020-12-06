directions = open('directions.txt', 'r')

arr = []
for direction in directions:
    arr.append(direction.split()[0])

# Correct Answers:
    # - Part 1: 938
    # - Part 2: 696


rowNum = [i for i in range(128)]

columnNum = [i for i in range(8)]


# ======= Part 2 =======
idList = []
highest = 0

for i in arr:
    x, y = i[:7], i[7:]
    
    currRow = rowNum
    currCol = columnNum
    
    for direction in x:
        firstHalf = currRow[:len(currRow) // 2]
        secondHalf = currRow[len(currRow) // 2:]

        if direction == 'F':
            currRow = firstHalf
        else:
            currRow = secondHalf

    for direction in y:
        firstHalf = currCol[:len(currCol) // 2]
        secondHalf = currCol[len(currCol) // 2:]
        if direction == 'L':
            currCol = firstHalf
        else:
            currCol = secondHalf
    
    ID = currRow[0] * 8 + currCol[0]
    if ID > highest:
        highest = ID
    idList.append(ID)

idList.sort()

mySeat = 0
for i in range(len(idList) - 1):
    if idList[i] + 1 == idList[i + 1] - 1:
        if idList[i] + 1 not in idList:       
            mySeat = idList[i] + 1
print(mySeat)


# ======= Part 1 =======
# highest = 0
# for i in arr:
#     x, y = i[:7], i[7:]
    
#     currRow = rowNum
#     currCol = columnNum
    
#     # print(x)
#     for direction in x:
#         firstHalf = currRow[:len(currRow) // 2]
#         secondHalf = currRow[len(currRow) // 2:]
#         # print(direction)
#         if direction == 'F':
#             currRow = firstHalf
#         else:
#             currRow = secondHalf
#         # print(currRow) 
#         # break
    
#     # print(currCol[:len(currCol) // 2], currCol[len(currCol) // 2:])
#     # break
#     for direction in y:
#         firstHalf = currCol[:len(currCol) // 2]
#         secondHalf = currCol[len(currCol) // 2:]
#         if direction == 'L':
#             currCol = firstHalf
#         else:
#             currCol = secondHalf
    
#     ID = currRow[0] * 8 + currCol[0]
#     if ID > highest:
#         highest = ID

# print(highest)
    

    # while len(currRow) > 1:
